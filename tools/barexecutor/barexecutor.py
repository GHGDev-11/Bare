import os
import sys
import re
import shutil
import subprocess
import requests
ptf=os.getcwd()
print(sys.argv)
def compile(content):
  return re.sub(r'[a-z]', lambda match: f"x{ord(match.group())-ord('a')+1}/", content)
def main():
    folder=f'{sys.argv[1][:-3]}'
    if not os.path.exists(folder):
        os.makedirs(f'{sys.argv[1][:-3]}')
        print(f"Created directory '{sys.argv[1][:-3]}'.")
    else:
        print(f"Output folder '{sys.argv[1][:-3]}' already exists. Please delete the folder and restart.\nPress ENTER to exit.")
        input()
        quit()
    print(f"Compiling script to {sys.argv[1][:-3]}.bac...")
    f=open(f'{sys.argv[1][:-3]}/{sys.argv[1][:-3]}.bac','w+')
    f.write(compile(open(sys.argv[1]).read()))
    print("Compiling completed.")
    f.close()
    source = "C:/Program Files (x86)/Bare/bare.exe"
    destination = f"{sys.argv[1][:-3]}/{sys.argv[1][:-3]}.exe"
    print(f"Preparing to compile {sys.argv[1][:-3]}.exe...")
    shutil.copy(source,destination)
    x=open(f'{sys.argv[1][:-3]}/{sys.argv[1][:-3]}.bac').read()
    print(f"Getting compiled script...")
    barescript=requests.get('https://raw.githubusercontent.com/GHGDev-11/Bare/main/bare.py').text.replace('run=sys.argv[1]',f'run="{sys.argv[1][:-3]}.bac"')
    m=open(f'{sys.argv[1][:-3]}/{sys.argv[1][:-3]}.py','w+').write(barescript)
    print(f"Starting compilation...")
    subprocess.call(f'include/pyinstaller --onefile --icon {sys.argv[2]} {sys.argv[1][:-3]}/{sys.argv[1][:-3]}.py')
    os.remove(f'{sys.argv[1][:-3]}/{sys.argv[1][:-3]}.py')
    print(f"Finalizing...")
    shutil.copy(f'dist/{sys.argv[1][:-3]}.exe',f'{sys.argv[1][:-3]}/{sys.argv[1][:-3]}.exe')
    print(f"Removing temporary help files...")
    os.remove(f'{sys.argv[1][:-3]}.spec')
    os.remove(f'{sys.argv[1][:-3]}/__pycache__/{sys.argv[1][:-3]}.cpython-38.pyc')
    os.rmdir(f'{sys.argv[1][:-3]}/__pycache__')
    os.remove(f'dist/{sys.argv[1][:-3]}.exe')
    os.rmdir('dist')
    os.chdir(f'build/{sys.argv[1][:-3]}')
    cptf=os.getcwd()
    for file in os.listdir(cptf):
        os.remove(file)
    os.chdir('..')
    os.rmdir(sys.argv[1][:-3])
    os.chdir('..')
    os.rmdir('build')
    print("Done!")
if __name__ == "__main__":
    main()