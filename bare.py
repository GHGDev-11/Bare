import os,sys,webbrowser,requests
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
class Error:
    def __init__(self,name,details):
        print(f"{name}:")
        print(f"    {details}")
class Evaluator:
    def __init__(self, file):
        self.keywords=['say','ask','hyperlink','lookup.key','readout','say-previously-read','__root__','__name__','__package__','__doc__','delete','__keywords__','get-html','make','use','__system_arguments__','__change_window_title__','start','open','write','close','write-previously-read','read','if','default:','__get_keywords__']
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
        self.consequences=''
        self.elseconsequences=''
        self.parameters=[]
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
                    elif word=='hyperlink':
                        v=line[10:].replace('"','').replace("'",'')
                        if not v.startswith('http'):
                            Error("InvalidLinkError",f"Link '{v}' does not start with 'http' or 'https', please include this or use lookup.key")
                        else:
                            webbrowser.open(v)
                    elif word=='lookup.key':
                        v=line[11:].replace('"','').replace("'",'')
                        if v.startswith('http'):
                            Error("InvalidLinkError",f"Keyword '{v}' starts with 'http' or 'https', please remove this or use hyperlink.")
                        else:
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
                                    v1=v1.replace('[','').replace(']','')
                                    if v1=='':
                                        p=os.getcwd()
                                    else:
                                        p=v1
                                else:
                                    vt=v1.replace('<','').replace('>','')
                        v=f'{p}\{vt}\{vt}.ba'
                        self.run(v)
                        self.imports.append(vt)
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
                    elif word=='if':
                        v=line[3:]
                        i=v.split(': ')
                        for r in i:
                            if r==i[1]:
                                c=r
                                question=i[0]
                                consequences=c.split(' & ')
                        for x in consequences:
                            self.consequences+=f'\n{x}'
                        Answer=False
                        Answer=eval(question)
                        if Answer==True:
                            b=open('if.BaRT','w+')
                            b.write(self.consequences)
                            b.close()
                            self.run('if.BaRT')
                            os.remove('if.BaRT')
                        else:
                            z=open('else.BaRT','w+')
                            z.write(self.elseconsequences)
                            z.close()
                            self.run('else.BaRT')
                            os.remove('else.BaRT')
                    elif word=='default:':
                        v=line[9:]
                        i=v.split(': ')
                        for r in i:
                            if r=='default':
                                i.remove(r)
                        h=str(i).replace('[','').replace(']','').replace("'",'').replace('"','').split(' & ')
                        for m in h:
                            self.elseconsequences+=f'\n{m}'
                    elif word=='__get_keywords__':
                        if 'allkeywords' in self.imports:
                            print(self.keywords)
                        else:
                            pass
                    else:
                        Error("InvalidArgumentError",f"Invalid argument: '{word}'")
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
                        self.runFunc(self.tasks,self.main)
                    else:
                        InvalidFunctionError(f"Invalid function '{word}'. Double check if you have spelled it right or have made it.")
                elif not word in self.keywords and "'" not in word and '"' not in word and word.startswith('<') and word.endswith('>'):
                    pass
                elif word in self.keywords:
                    pass
                else:
                    Error("GrammarError",f"Bad grammar: {word}")
        f.close()
        os.remove(f'${name}.BaRT')
    def run(self,file):
        f=open(file, 'r')
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
                    elif word=='hyperlink':
                        v=line[10:].replace('"','').replace("'",'')
                        if not v.startswith('http'):
                            Error("InvalidLinkError",f"Link '{v}' does not start with 'http' or 'https', please include this or use lookup.key")
                        else:
                            webbrowser.open(v)
                    elif word=='lookup.key':
                        v=line[11:].replace('"','').replace("'",'')
                        if v.startswith('http'):
                            Error("InvalidLinkError",f"Keyword '{v}' starts with 'http' or 'https', please remove this or use hyperlink.")
                        else:
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
                        self.imports.append(vt)
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
                    elif word=='if':
                        v=line[3:]
                        i=v.split(': ')
                        for r in i:
                            if r==i[1]:
                                c=r
                                question=i[0]
                                consequences=c.split(' | ')
                        for x in consequences:
                            self.consequences+=f'\n{x}'
                        Answer=False
                        Answer=eval(question)
                        if Answer==True:
                            b=open('if.BaRT','w+')
                            b.write(self.consequences)
                            b.close()
                            self.run('if.BaRT')
                            os.remove('if.BaRT')
                        else:
                            z=open('else.BaRT','w+')
                            z.write(self.elseconsequences)
                            z.close()
                            self.run('else.BaRT')
                            os.remove('else.BaRT')
                    elif word=='default:':
                        v=line[9:]
                        h=v.split(' | ')
                        for m in h:
                            self.elseconsequences+=f'\n{m}'
                    elif word=='__get_keywords__':
                        if 'allkeywords' in self.imports:
                            print(self.keywords)
                        else:
                            pass
                    else:
                        Error("InvalidArgumentError",f"Invalid argument: '{word}'")
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
                elif word not in self.keywords and '"' not in word and "'" not in word and 'if' in line:
                    pass
                elif '-' in word:
                    pass
                else:
                    Error("GrammarError",f"Bad grammar: {word}")
run=sys.argv[1]
import re
def decompile(content):
  return re.sub(r'x(\d+)/', lambda match: chr(int(match.group(1))-1+ord('a')), content)
def main():
    if run.endswith('.bac'):
        decompile(open(run,'r').read())
        FileRun=run.replace('.bac','')
        decomp=open(f'{FileRun}.ba','w+')
        decomp.write(decompile(open(run,'r').read()))
        decomp.close()
        ev=Evaluator(f'{FileRun}.ba')
        ev.run(f'{FileRun}.ba')
        os.remove(f'{FileRun}.ba')
    else:
        ev=Evaluator(run)
        ev.run(run)
main()
