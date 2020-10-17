import os
import webbrowser
import requests
import sys
class InvalidArgumentError:
    def __init__(self,details):
        print("InvalidArgumentError:")
        print(f"    {details}")
        input()
class GrammarError:
    def __init__(self,details):
        print("GrammarError:")
        print(f"    {details}")
        input()
class InvalidLinkError:
    def __init__(self,details):
        print("InvalidLinkError:")
        print(f"    {details}")
        input()
class InvalidLinkSettingError:
    def __init__(self,details):
        print("InvalidLinkSettingError:")
        print(f"    {details}")
        input()
class InvalidFunctionError:
    def __init__(self,details):
        print("InvalidFunctionError:")
        print(f"    {details}")
        input()
class UseError:
    def __init__(self,details):
        print("UseError:")
        print(f"    {details}")
        input()
class Evaluator:
    def __init__(self, file):
        self.keywords=['say','ask','lookup.link','lookup.key','lookup.all','readout','say-previously-read','__root__','__name__','__package__','__doc__','delete','__keywords__','get-html','make','use','__system_arguments__','__change_window_title__','start','open','write','close','write-previously-read','read']
        self.__file__=file
        self.r=None
        self.root=__file__
        self.name=__name__
        self.package=__package__
        self.doc=__doc__
        self.n=None
        self.p=None
        self.main=None
        self.mainlen=None
        self.mainname=None
        self.tasks=''
        self.imports=[]
        self.importname=None
        self.loop=''
        self.read=''
    def runFunc(self,function,name):
        f=open(f'${name}.BaRT','w+')
        f.write(function)
        f.seek(0)
        function=f.readlines()
        lines=(line.rstrip() for line in function)
        lines=list(line for line in lines if line)
        for line in lines:
            words=line.split(' ')
            for word in words:
                if word in self.keywords and '"' not in word and "'" not in word:
                    if word=='say':
                        ra=line[4:].replace('"','').replace("'",'')
                        v=ra.replace('-v','\n')
                        print(v)
                    elif word=='ask':
                        v=line[4:].replace('"','').replace("'",'')
                        input(v)
                    elif word=='start':
                        v=line[6:].replace('"','').replace("'",'')
                        os.startfile(v)
                    elif word=='lookup.link':
                        v=line[12:].replace('"','').replace("'",'')
                        if not v.startswith('http'):
                            InvalidLinkError(f"Link '{v}' does not start with 'http' or 'https', please include this or use lookup.key")
                        else:
                            webbrowser.open(v)
                    elif word=='lookup.key':
                        v=line[11:].replace('"','').replace("'",'')
                        if v.startswith('http'):
                            InvalidLinkError(f"Keyword '{v}' starts with 'http' or 'https', please remove this or use lookup.all")
                        else:
                            webbrowser.open(v)
                    elif word=='lookup.all':
                        v=line[11:].replace('"','').replace("'",'')
                        webbrowser.open(v)
                    elif word=='readout':
                        v=line[8:].replace('"','').replace("'",'').replace('\n','')
                        f=open(v,'r')
                        self.r=f.read()
                        f.close()
                        print(self.r)
                    elif word=='say-previously-read':
                        print(self.r)
                    elif word=='__root__':
                        print(self.root)
                    elif word=='__name__':
                        print(self.name)
                    elif word=='__package__':
                        print(self.package)
                    elif word=='__doc__':
                        print(self.doc)
                    elif word=='__keywords__':
                        v=len(self.keywords)
                        print(v)
                    elif word=='delete':
                        v=line[7:].replace('"','').replace("'",'')
                        os.remove(v)
                    elif word=='get-html':
                        v=line[9:].replace('"','').replace("'",'')
                        z=requests.get(v)
                        c=z.text
                        print(c)
                    elif word=='make':
                        v=line[5:]
                        l=v.split(': ')
                        for i in l:
                            if '$' in i:
                                self.mainlen=len(i)
                                self.mainname=i.replace('$','')
                            else:
                                ts=i.split(' | ')
                                for t in ts:
                                    self.tasks+=f'\n{t}'
                        self.main=l[1]
                    elif word=='use':
                        r=line[4:]
                        if '-> ' in r:
                            v2=r.split(' -> ')
                            for v1 in v2:
                                if v1.startswith('[') and v1.endswith(']'):
                                    p=v1.replace('[','').replace(']','')
                                    print(p)
                                else:
                                    vt=v1.replace('<','').replace('>','')
                        v=f'{p}\{vt}\{vt}.ba'
                        self.run(v)
                    elif word=='__system_arguments__':
                        v=sys.argv
                        for arg in v:
                            if 'bare.exe' in arg or 'bare.py' in arg:
                                v.remove(arg)
                        print(v)
                    elif word=='__change_window_title__':
                        nr=sys.argv[1]
                        n=nr.split('.')
                        for g in n:
                            if g=='ba':
                                n.remove(g)
                        na=str(n)
                        nam=na.replace('[','').replace(']','').replace("'",'')
                        os.system(f"title {nam}")
                    elif word=='open':
                        v=line[5:].replace("'",'').replace('"','')
                        self.openfile=open(v,'w+')
                    elif word=='write':
                        v=line[6:].replace("'",'').replace('"','')
                        self.openfile.write(v)
                    elif word=='close':
                        v=line[6:].replace("'",'').replace('"','')
                        self.openfile.close()
                    elif word=='read':
                        v=line[5:].replace("'",'').replace('"','')
                        h=open(v,'r')
                        self.read=h.read()
                    elif word=='write-previously-read':
                        v=line[22:].replace("'",'').replace('"','')
                        j=open(v,'w')
                        j.write(self.read)
                    else:
                        InvalidArgumentError(f"Invalid argument: '{word}'")
                elif not word in self.keywords and "'" not in word and '"' in word:
                    pass
                elif not word in self.keywords and '"' not in word and "'" in word:
                    pass
                elif not word in self.keywords and '"' not in word and "'" not in word and '"' in line and "'" not in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and "'" in line and '"' not in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and '"' in line and "'" not in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and "'" in line and '"' in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and '$' in line:
                    if word==f'${self.mainname}':
                        self.runFunc(self.tasks,self.mainname)
                    else:
                        InvalidFunctionError(f"Invalid function '{word}'. Double check if you have spelled it right or have made it.")
                elif not word in self.keywords and "'" not in word and '"' not in word and word.startswith('<') and word.endswith('>'):
                    pass
                elif word in self.keywords:
                    pass
                else:
                    GrammarError(f"Wrong grammar usage: '{word}'. Word is not found in our keywords, and isn't quoted.")
                    goodGrammar=False
        f.close()
        os.remove(f'${name}.BaRT')
    def run(self,string):
        f=open(string, 'w+')
        f.write(string)
        f.seek(0)
        content=f.readlines()
        lines=(line.rstrip() for line in content)
        lines=list(line for line in lines if line)
        for line in lines:
            words=line.split(' ')
            for word in words:
                if word in self.keywords and '"' not in word and "'" not in word and line.startswith(word):
                    line.replace('-v','\n')
                    if word=='say':
                        v=line[4:].replace('"','').replace("'",'')
                        print(v)
                    elif word=='ask':
                        v=line[4:].replace('"','').replace("'",'')
                        input(v)
                    elif word=='start':
                        v=line[6:].replace('"','').replace("'",'')
                        os.startfile(v)
                    elif word=='lookup.link':
                        v=line[12:].replace('"','').replace("'",'')
                        if not v.startswith('http'):
                            InvalidLinkError(f"Link '{v}' does not start with 'http' or 'https', please include this or use lookup.key")
                        else:
                            webbrowser.open(v)
                    elif word=='lookup.key':
                        v=line[11:].replace('"','').replace("'",'')
                        if v.startswith('http'):
                            InvalidLinkError(f"Keyword '{v}' starts with 'http' or 'https', please remove this or use lookup.all")
                        else:
                            webbrowser.open(v)
                    elif word=='lookup.all':
                        v=line[11:].replace('"','').replace("'",'')
                        webbrowser.open(v)
                    elif word=='readout':
                        v=line[8:].replace('"','').replace("'",'').replace('\n','')
                        f=open(v,'r')
                        self.r=f.read()
                        print(self.r)
                    elif word=='say-previously-read':
                        print(self.r)
                    elif word=='__root__':
                        print(self.root)
                    elif word=='__name__':
                        print(self.name)
                    elif word=='__package__':
                        print(self.package)
                    elif word=='__doc__':
                        print(self.doc)
                    elif word=='__keywords__':
                        v=len(self.keywords)
                        print(v)
                    elif word=='delete':
                        v=line[7:].replace('"','').replace("'",'')
                        os.remove(v)
                    elif word=='get-html':
                        v=line[9:].replace('"','').replace("'",'')
                        z=requests.get(v)
                        c=z.text
                        print(c)
                    elif word=='make':
                        v=line[5:]
                        l=v.split(': ')
                        for i in l:
                            if '$' in i:
                                self.mainlen=len(i)
                                self.mainname=i.replace('$','')
                            else:
                                ts=i.split(' | ')
                                for t in ts:
                                    self.tasks+=f'\n{t}'
                        self.main=l[1]
                    elif word=='use':
                        r=line[4:]
                        if '-> ' in r:
                            v2=r.split(' -> ')
                            for v1 in v2:
                                if v1.startswith('[') and v1.endswith(']'):
                                    v1=v1.replace('[','').replace(']','')
                                    if v1=='':
                                        p=os.getcwd()
                                    else:
                                        p=v1
                                else:
                                    vt=v1.replace('<','').replace('>','')
                        v=f'{p}\{vt}\{vt}.ba'
                        self.run(v)
                    elif word=='__system_arguments__':
                        v=sys.argv
                        for arg in v:
                            if 'bare.exe' in arg or 'bare.py' in arg:
                                v.remove(arg)
                        print(v)
                    elif word=='__change_window_title__':
                        nr=sys.argv[2]
                        n=nr.split('.')
                        for g in n:
                            if g=='ba':
                                n.remove(g)
                        na=str(n)
                        nam=na.replace('[','').replace(']').replace("'",'')
                        os.system(f"title {nam}")
                    elif word=='open':
                        v=line[5:].replace("'",'').replace('"','')
                        self.openfile=open(v,'w+')
                    elif word=='write':
                        v=line[6:].replace("'",'').replace('"','')
                        self.openfile.write(v)
                    elif word=='close':
                        v=line[6:].replace("'",'').replace('"','')
                        self.openfile.close()
                    elif word=='read':
                        v=line[5:].replace("'",'').replace('"','')
                        h=open(v,'r')
                        self.read=h.read()
                    elif word=='write-previously-read':
                        v=line[22:].replace("'",'').replace('"','')
                        j=open(v,'w')
                        j.write(self.read)
                    else:
                        InvalidArgumentError(f"Invalid argument: '{word}'")
                elif not word in self.keywords and "'" not in word and '"' in word:
                    pass
                elif not word in self.keywords and '"' not in word and "'" in word:
                    pass
                elif not word in self.keywords and '"' not in word and "'" not in word and '"' in line and "'" not in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and "'" in line and '"' not in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and '"' in line and "'" not in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and "'" in line and '"' in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and '$' in line:
                    if word==f'${self.mainname}':
                        self.runFunc(self.tasks,self.mainname)
                elif not word in self.keywords and "'" not in word and '"' not in word and word.startswith('<') and word.endswith('>'):
                    pass
                elif word in self.keywords:
                    pass
                elif word not in self.keywords and '"' not in word and "'" not in word and ':' in line:
                    pass
                else:
                    GrammarError(f"Wrong grammar usage: '{word}'. Word is not found in our keywords, and isn't quoted.")
                    goodGrammar=False
run=''
import re
def decompile(content):
  return re.sub(r'x(\d+)/', lambda match: chr(int(match.group(1))-1+ord('a')), content)
def main():
    try:
        ev=Evaluator(run)
        ev.run(run)
    except:
        print("Prevented crash.")
        GrammarError(f"Wrong grammar usage: '{word}'. Word is not found in our keywords, and isn't quoted.")
print("Bareline - Bare")
print("Made by Georges Abdulahad")
while True:
    run=input(f'>>> ')
    main()
