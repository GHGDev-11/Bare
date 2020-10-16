import re

def compile(content):
  return re.sub(r'[a-z]', lambda match: f"x{ord(match.group())-ord('a')+1}/", content)

import sys
if __name__ == "__main__":
    c=compile(open(sys.argv[1]).read())
    a=sys.argv[1].split('.')
    for i in a:
        if i=='ba':
            a.remove(i)
    u=str(a).replace('[','').replace(']','').replace("'",'')
    f=open(f'{u}.bac','w+')
    f.write(c)
    f.close()