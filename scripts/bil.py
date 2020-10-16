import sys
import requests
import webbrowser
import os
if len(sys.argv) < 2:
    print("Syntax: [Command] [Atom]")
else:
    pass
def main(cmd,atom):
    if cmd=='get':
        tries=0
        success=False
        a=requests.get('https://pastebin.com/raw/wHW7Awi4')
        pkg=a.text
        f=open('bil.BaI','w+')
        f.write(pkg)
        f.seek(0)
        lines=f.readlines()
        f.close()
        os.remove('bil.BaI')
        for link in lines:
            if f'https://github.com/GHGDev-11/{atom}' in link:
                success=True
                webbrowser.open(link)
                print(f'Installing {atom}...')
            else:
                tries+=1
                success=False
        print(f'Total tries: {tries}')
    else:
        print(f"Command '{cmd}' is not a valid installing command.")
if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])