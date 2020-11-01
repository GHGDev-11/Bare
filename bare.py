import os,sys,webbrowser,requests,pickle,tempfile,re
goodGrammar=True
class Error:
    def __init__(self,name,details,ln,wn,fn):
        global goodGrammar
        if goodGrammar==False:
            print("\nDuring this error, another error occurred:\n")
        print("Error (Most recent is shown last):")
        print(f"  File '<{fn}>',")
        print(f"    Line {ln}, word {wn}:")
        print(f"{name}:")
        print(f"    {details}")
        input()
        goodGrammar=False
class Decompiler:
    def __init__(self,file):
        with open(file, 'rb') as loading:
            fr=pickle.load(loading)
        a1=fr.replace('111111---','a')
        a2=a1.replace('111110---','b')
        a3=a2.replace('111100---','c')
        a4=a3.replace('111000---','d')
        a5=a4.replace('110000---','e')
        a6=a5.replace('100000---','f')
        a7=a6.replace('000000---','g')
        a8=a7.replace('000001---','h')
        a9=a8.replace('000010---','i')
        a10=a9.replace('000100---','j')
        a11=a10.replace('001000---','k')
        a12=a11.replace('010000---','l')
        a13=a12.replace('101000---','m')
        a14=a13.replace('101010---','n')
        a15=a14.replace('111010---','o')
        a16=a15.replace('111011---','p')
        a17=a16.replace('010101---','q')
        a18=a17.replace('011101---','r')
        a19=a18.replace('011110---','s')
        a20=a19.replace('001100---','t')
        a21=a20.replace('001110---','u')
        a22=a21.replace('001111---','v')
        a23=a22.replace('001010---','w')
        a24=a23.replace('000110---','x')
        a25=a24.replace('010011---','y')
        self.a26=a25.replace('010110---','z')
    def get(self):
        return self.a26
    def write(self,a):
        self.currentatom=f'{a[:-3]}'
        self.f=open(self.currentatom,'w+')
        self.f.write(self.get())
        print(self.f.read())
        self.f.close()
        return self.currentatom
    def finalize(self):
        self.f.close()
        os.remove(self.currentatom)
class Compiler:
    def __init__(self,file):
        fsd=open(file,'r').read()
        a1=fsd.replace('a','111111---')
        a2=a1.replace('b','111110---')
        a3=a2.replace('c','111100---')
        a4=a3.replace('d','111000---')
        a5=a4.replace('e','110000---')
        a6=a5.replace('f','100000---')
        a7=a6.replace('g','000000---')
        a8=a7.replace('h','000001---')
        a9=a8.replace('i','000010---')
        a10=a9.replace('j','000100---')
        a11=a10.replace('k','001000---')
        a12=a11.replace('l','010000---')
        a13=a12.replace('m','101000---')
        a14=a13.replace('n','101010---')
        a15=a14.replace('o','111010---')
        a16=a15.replace('p','111011---')
        a17=a16.replace('q','010101---')
        a18=a17.replace('r','011101---')
        a19=a18.replace('s','011110---')
        a20=a19.replace('t','001100---')
        a21=a20.replace('u','001110---')
        a22=a21.replace('v','001111---')
        a23=a22.replace('w','001010---')
        a24=a23.replace('x','000110---')
        a25=a24.replace('y','010011---')
        self.a26=a25.replace('z','010110---')
    def get(self):
        return self.a26
def BacCompiler(content):
    return re.sub(r'[a-z]', lambda match: f"x{ord(match.group())-ord('a')+1}/", content)
class Evaluator:
    def __init__(self, file):
        self.keywords=['say','ask','hyperlink','readout','say-previously-read','__root__','__name__','__package__','__doc__','delete','__keywords__','get-html','make','use','__system_arguments__','__change_window_title__','start','open','write','close','write-previously-read','read','if','default:','__get_keywords__','read-current','set-cursor','compile_atom','compile','var','__change_window_title_WE__','nothing','__QUIT_EXIT__']
        self.__file__=file
        self.r=None
        self.root=__file__
        self.name=__name__
        self.package=__package__
        self.doc=__doc__
        self.imports=[]
        self.read=''
        self.consequences=''
        self.elseconsequences=''
        self.registers=[]
        self.specialchars=['->','[]']
        self.ln=0
        self.wn=0
    def RunKey(self,key,v):
        if not "'" in v and not '"' in v:
            try:
                if v!=' ' and v!='':
                    exec(key)
                else:
                    pass
            except:
                Error("InvalidVariableError",f"Variable '{v}' does not exist.\n{' '*14}{'~'*(len(v)-2)}\n{' '*14}^",self.ln,self.wn,self.__file__)
        else:
            exec(key.replace('self.',''))
    def runFunc(self,function,name):
        f=open(f'${name}.BaRT','w+')
        f.write(function)
        f.seek(0)
        function=f.readlines()
        lines=(line.rstrip() for line in function)
        lines=list(line for line in lines if line)
        lines=list(line for line in lines if not line.startswith('||'))
        for line in lines:
            self.ln+=1
            words=line.split(' ')
            for word in words:
                self.wn+=1
                if word in self.keywords and '"' not in word and "'" not in word and line.startswith(word):
                    if word=='say':
                        v=line[4:]
                        self.RunKey(f'print(self.{v})',v)
                    elif word=='ask':
                        if len(line)>4:
                            v=line[4:]
                            self.RunKey(f'input(self.{v})',v)
                        else:
                            input()
                    elif word=='start':
                        v=line[6:]
                        self.RunKey(f"try:\n    os.startfile(self.{v})\nexcept FileNotFoundError:\n    Error('UnknownFileError',f\"Could not find file or directory '{v}'.\\n{' '*38}{'~'*len(v)}\\n{' '*38}^\",self.ln,self.wn,self.__file__)",v)
                    elif word=='hyperlink':
                        v=line[10:].replace('"','').replace("'",'')
                        self.RunKey(f"try:\n    webbrowser.open(self.{v})\nexcept ConnectionError:\n    Error('ConnectionError',f\"Link '{v}' may not start with 'http' or 'https', please include this. If your link is correct, check if you are connected to the internet.\\n{' '*10}{'~'*len(v)}\\n{' '*10}\",self.ln,self.wn,self.__file__)",v)
                    elif word=='readout':
                        v=line[8:]
                        self.RunKey(f"try:\n    f=open(self.{v},'r')\n    self.r=f.read()\n    print(self.r)\nexcept FileNotFoundError:\n    Error(\"InvalidFileError\",f\"Could not find file '{v}'. Have you spelled it right?\\n{' '*25}{'~'*len(v)}\\n{' '*25}^\",self.ln,self.wn,self.__file__)",v)
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
                        print(len(self.keywords))
                    elif word=='delete':
                        v=line[7:]
                        self.RunKey(f'try:\n    os.remove(self.{v})\nexcept:\n    Error("InvalidFileError",f"Could not find file \'{v[1:][:-1]}\'. Have you spelled it right?\\n{" "*25}{"~"*(len(v)-2)}\\n{" "*25}^",self.ln,self.wn,self.__file__)',v)
                    elif word=='get-html':
                        v=line[9:]
                        self.RunKey(f'try:\n    z=requests.get(self.{v})\n    c=z.text\n    print(c)\nexcept requests.exceptions.ConnectionError:\n    Error("URLError",f"Could not connect to URL \'{v[1:][:-1]}\'. If the given link is correct, please check your internet connection.\\n{" "*30}{"~"*(len(v)-2)}\\n{" "*30}^",self.ln,self.wn,self.__file__)',v)
                    elif word=='make':
                        v=line[5:]
                        l=v.split(': ')
                        im=l[0]
                        mainlen=len(im)
                        mainname=im.replace('$','')
                        try:
                            ix=l[1]
                            ts=ix.replace(' | ','\\n')
                            if len(l)>1:
                                exec(f'self.{im[1:]}="{ts}"')
                            self.registers.append(f'self.{im[1:]}')
                        except IndexError:
                            Error("EmptyFunctionError",f"Empty function; if you don't want your function to do anything, use the keyword 'nothing'.",self.ln,self.wn,self.__file__)
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
                        try:
                            v=f'{p}\{vt}'
                            for filename in os.listdir(v):
                                if filename.endswith('.batom'):
                                    useDeco=Decompiler(f'{v}\\{filename}')
                                    dcfile=useDeco.write(f'{v}\\{filename}')
                                    self.run(dcfile)
                                    useDeco.finalize()
                                    self.imports.append(vt)
                                elif filename.endswith('.ba'):
                                    self.run(f'{v}\\{filename}')
                                    self.imports.append(vt)
                                elif filename=='config.txt':
                                    f=open(f'{v}\config.txt','r').readlines()
                                    for c in f:
                                        c=c.replace(' ','')
                                        q=c.split('=')
                                        for i in q:
                                            if i=='readme-file':
                                                rmf=q[1].replace("'",'').replace('"','')
                                                print(open(f'{v}\{rmf}','r').read())
                                else:
                                    pass
                        except UnboundLocalError:
                            Error("SyntaxError",f"{line}\n{' '*8}{'~'*len(r)}\n{' '*8}^",self.ln,self.wn,self.__file__)
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
                            if g=='ba' or g=='bac':
                                n.remove(g)
                        na=str(n)
                        nam=na.replace('[','').replace(']','').replace("'",'')
                        os.system(f"title {nam}")
                    elif word=='__change_window_title_WE__':
                        nr=sys.argv[1]
                        os.system(f"title {nr}")
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
                    elif word=='read-current':
                        try:
                            self.read=self.openfile.read()
                        except AttributeError:
                            Error("UnopenFileError",f"Could not execute keyword read-current, because you do not have a file open.",self.ln,self.wn,self.__file__)
                    elif word=='set-cursor':
                        try:
                            v=int(line[11:].replace('(','').replace(')',''))
                            self.openfile.seek(v)
                        except AttributeError:
                            Error("UnopenFileError",f"Could not set cursor at location '{line[11:]}', because you do not have a file open.",self.ln,self.wn,self.__file__)
                        except:
                            Error("SetCursorError",f"Could not set cursor at location '{line[11:]}', because it is not a number.",self.ln,self.wn,self.__file__)
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
                    elif word=='compile_atom':
                        af=line[13:].split(' ')
                        a2=af[0].replace("'",'').replace('"','')
                        if len(af)<2:
                            fsd=open(a2,'r')
                            atomc=Compiler(a2)
                        else:
                            p=af[1].replace("'",'').replace('"','')
                            fsd=open(a2,'r')
                            atomc=Compiler(a2)
                        fssr=fsd.read()
                        a26=''
                        print("Initializing compiler...")
                        bytsc=atomc.get()
                        try:
                            with open(f'{p}\\{os.path.basename(a2[:-3])}.batom','wb') as f:
                                pickle.dump(bytsc,f,protocol=2)
                            print(f"Finished compiling '{a2}'!\nPath:\n    {p}\\{a2[:-3]}.batom")
                        except UnboundLocalError:
                            Error("SyntaxError",f"{line}\n{' '*18}{'~'*len(line[15:])}\n{' '*18}^",self.ln,self.wn,self.__file__)
                    elif word=='compile':
                        v=line[8:].replace('"','').replace("'",'')
                        f=open(v,'r')
                        fr=f.read()
                        kj=open(f'{os.path.splitext(v)[0]}.bac','w+')
                        kj.write(BacCompiler(fr))
                        kj.close()
                    elif word=='var':
                        v=line[4:]
                        vlist=v.split('=')
                        con=vlist[1].replace('"','').replace("'",'')
                        va=vlist[0]
                        exec(f'self.{va}="{con}"')
                        self.registers.append(va)
                    elif word=='nothing':
                        pass
                    elif word=='__QUIT_EXIT__':
                        sys.exit()
                    else:
                        Error("InvalidArgumentError",f"Invalid argument: '{word}'\n{' '*23}{'~'*len(word)}\n{' '*23}^",self.ln,self.wn,self.__file__)
                elif not word in self.keywords and "'" in word and '"' not in word:
                    pass
                elif not word in self.keywords and "'" not in word and '"' in word:
                    pass
                elif not word in self.keywords and '"' not in word and "'" not in word and '"' in line or "'" in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and '"' in line and "'" not in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and "'" in line and '"' in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and '$' in line:
                    if word.startswith('$') and line.startswith(word):
                        try:
                            exec(f'self.runFunc(self.{word[1:]},word)')
                        except AttributeError:
                            Error("InvalidFunctionError",f"Function '{word[1:]}' does not exist.\n{' '*14}{'~'*(len(word)-1)}\n{' '*14}^",self.ln,self.wn,self.__file__)
                elif not word in self.keywords and "'" not in word and '"' not in word and word.startswith('<') and word.endswith('>'):
                    pass
                elif word in self.keywords:
                    pass
                elif word not in self.keywords and '"' not in word and "'" not in word and ':' in line:
                    pass
                elif word not in self.keywords and '"' not in word and "'" not in word and 'if' in line:
                    pass
                elif word in self.registers:
                    pass
                elif not word in self.keywords and word.startswith('(') and word.endswith(')'):
                    pass
                elif word not in self.keywords and line.startswith('var'):
                    pass
                elif word not in self.keywords and word in self.specialchars:
                    pass
                elif word==' ' or word=='':
                    pass
                else:
                    Error("GrammarError",f"Bad grammar: '{word}'\n{' '*18}{'~'*len(word)}\n{' '*18}^",self.ln,self.wn,self.__file__)
        f.close()
        os.remove(f'${name}.BaRT')
    def run(self,file):
        runningfile=open(file, 'r')
        content=runningfile.readlines()
        lines=(line.rstrip() for line in content)
        lines=list(line for line in lines if line)
        lines=list(line for line in lines if not line.startswith('||'))
        for line in lines:
            self.ln+=1
            words=line.split(' ')
            for word in words:
                self.wn+=1
                if word in self.keywords and '"' not in word and "'" not in word and line.startswith(word):
                    if word=='say':
                        v=line[4:]
                        self.RunKey(f'print(self.{v})',v)
                    elif word=='ask':
                        if len(line)>4:
                            v=line[4:]
                            self.RunKey(f'input(self.{v})',v)
                        else:
                            input()
                    elif word=='start':
                        v=line[6:]
                        self.RunKey(f"try:\n    os.startfile(self.{v})\nexcept FileNotFoundError:\n    Error('UnknownFileError',f\"Could not find file or directory '{v}'.\\n{' '*38}{'~'*len(v)}\\n{' '*38}^\",self.ln,self.wn,self.__file__)",v)
                    elif word=='hyperlink':
                        v=line[10:].replace('"','').replace("'",'')
                        self.RunKey(f"try:\n    webbrowser.open(self.{v})\nexcept ConnectionError:\n    Error('ConnectionError',f\"Link '{v}' may not start with 'http' or 'https', please include this. If your link is correct, check if you are connected to the internet.\\n{' '*10}{'~'*len(v)}\\n{' '*10}\",self.ln,self.wn,self.__file__)",v)
                    elif word=='readout':
                        v=line[8:]
                        self.RunKey(f"try:\n    f=open(self.{v},'r')\n    self.r=f.read()\n    print(self.r)\nexcept FileNotFoundError:\n    Error(\"InvalidFileError\",f\"Could not find file '{v}'. Have you spelled it right?\\n{' '*25}{'~'*len(v)}\\n{' '*25}^\",self.ln,self.wn,self.__file__)",v)
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
                        print(len(self.keywords))
                    elif word=='delete':
                        v=line[7:]
                        self.RunKey(f'try:\n    os.remove(self.{v})\nexcept:\n    Error("InvalidFileError",f"Could not find file \'{v[1:][:-1]}\'. Have you spelled it right?\\n{" "*25}{"~"*(len(v)-2)}\\n{" "*25}^",self.ln,self.wn,self.__file__)',v)
                    elif word=='get-html':
                        v=line[9:]
                        self.RunKey(f'try:\n    z=requests.get(self.{v})\n    c=z.text\n    print(c)\nexcept requests.exceptions.ConnectionError:\n    Error("URLError",f"Could not connect to URL \'{v[1:][:-1]}\'. If the given link is correct, please check your internet connection.\\n{" "*30}{"~"*(len(v)-2)}\\n{" "*30}^",self.ln,self.wn,self.__file__)',v)
                    elif word=='make':
                        v=line[5:]
                        l=v.split(': ')
                        im=l[0]
                        mainlen=len(im)
                        mainname=im.replace('$','')
                        try:
                            ix=l[1]
                            ts=ix.replace(' | ','\\n')
                            if len(l)>1:
                                exec(f'self.{im[1:]}="{ts}"')
                            self.registers.append(f'self.{im[1:]}')
                        except IndexError:
                            Error("EmptyFunctionError",f"Empty function; if you don't want your function to do anything, use the keyword 'nothing'.",self.ln,self.wn,self.__file__)
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
                        try:
                            v=f'{p}\{vt}'
                            for filename in os.listdir(v):
                                if filename.endswith('.batom'):
                                    useDeco=Decompiler(f'{v}\\{filename}')
                                    dcfile=useDeco.write(f'{v}\\{filename}')
                                    self.run(dcfile)
                                    useDeco.finalize()
                                    self.imports.append(vt)
                                elif filename.endswith('.ba'):
                                    self.run(f'{v}\\{filename}')
                                    self.imports.append(vt)
                                elif filename=='config.txt':
                                    f=open(f'{v}\config.txt','r').readlines()
                                    for c in f:
                                        c=c.replace(' ','')
                                        q=c.split('=')
                                        for i in q:
                                            if i=='readme-file':
                                                rmf=q[1].replace("'",'').replace('"','')
                                                print(open(f'{v}\{rmf}','r').read())
                                else:
                                    pass
                        except UnboundLocalError:
                            Error("SyntaxError",f"{line}\n{' '*8}{'~'*len(r)}\n{' '*8}^",self.ln,self.wn,self.__file__)
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
                            if g=='ba' or g=='bac':
                                n.remove(g)
                        na=str(n)
                        nam=na.replace('[','').replace(']','').replace("'",'')
                        os.system(f"title {nam}")
                    elif word=='__change_window_title_WE__':
                        nr=sys.argv[1]
                        os.system(f"title {nr}")
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
                    elif word=='read-current':
                        try:
                            self.read=self.openfile.read()
                        except AttributeError:
                            Error("UnopenFileError",f"Could not execute keyword read-current, because you do not have a file open.",self.ln,self.wn,self.__file__)
                    elif word=='set-cursor':
                        try:
                            v=int(line[11:].replace('(','').replace(')',''))
                            self.openfile.seek(v)
                        except AttributeError:
                            Error("UnopenFileError",f"Could not set cursor at location '{line[11:]}', because you do not have a file open.",self.ln,self.wn,self.__file__)
                        except:
                            Error("SetCursorError",f"Could not set cursor at location '{line[11:]}', because it is not a number.",self.ln,self.wn,self.__file__)
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
                    elif word=='compile_atom':
                        af=line[13:].split(' ')
                        a2=af[0].replace("'",'').replace('"','')
                        if len(af)<2:
                            fsd=open(a2,'r')
                            atomc=Compiler(a2)
                        else:
                            p=af[1].replace("'",'').replace('"','')
                            fsd=open(a2,'r')
                            atomc=Compiler(a2)
                        fssr=fsd.read()
                        a26=''
                        print("Initializing compiler...")
                        bytsc=atomc.get()
                        try:
                            with open(f'{p}\\{os.path.basename(a2[:-3])}.batom','wb') as f:
                                pickle.dump(bytsc,f,protocol=2)
                            print(f"Finished compiling '{a2}'!\nPath:\n    {p}\\{a2[:-3]}.batom")
                        except UnboundLocalError:
                            Error("SyntaxError",f"{line}\n{' '*18}{'~'*len(line[15:])}\n{' '*18}^",self.ln,self.wn,self.__file__)
                    elif word=='compile':
                        v=line[8:].replace('"','').replace("'",'')
                        f=open(v,'r')
                        fr=f.read()
                        kj=open(f'{os.path.splitext(v)[0]}.bac','w+')
                        kj.write(BacCompiler(fr))
                        kj.close()
                    elif word=='var':
                        v=line[4:]
                        vlist=v.split('=')
                        con=vlist[1].replace('"','').replace("'",'')
                        va=vlist[0]
                        exec(f'self.{va}="{con}"')
                        self.registers.append(va)
                    elif word=='nothing':
                        pass
                    elif word=='__QUIT_EXIT__':
                        sys.exit()
                    else:
                        Error("InvalidArgumentError",f"Invalid argument: '{word}'\n{' '*23}{'~'*len(word)}\n{' '*23}^",self.ln,self.wn,self.__file__)
                elif not word in self.keywords and "'" in word and '"' not in word:
                    pass
                elif not word in self.keywords and "'" not in word and '"' in word:
                    pass
                elif not word in self.keywords and '"' not in word and "'" not in word and '"' in line or "'" in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and '"' in line and "'" not in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and "'" in line and '"' in line:
                    pass
                elif not word in self.keywords and "'" not in word and '"' not in word and '$' in line:
                    if word.startswith('$') and line.startswith(word):
                        try:
                            exec(f'self.runFunc(self.{word[1:]},word)')
                        except AttributeError:
                            Error("InvalidFunctionError",f"Function '{word[1:]}' does not exist.\n{' '*14}{'~'*(len(word)-1)}\n{' '*14}^",self.ln,self.wn,self.__file__)
                elif not word in self.keywords and "'" not in word and '"' not in word and word.startswith('<') and word.endswith('>'):
                    pass
                elif word in self.keywords:
                    pass
                elif word not in self.keywords and '"' not in word and "'" not in word and ':' in line:
                    pass
                elif word not in self.keywords and '"' not in word and "'" not in word and 'if' in line:
                    pass
                elif word in self.registers:
                    pass
                elif not word in self.keywords and word.startswith('(') and word.endswith(')'):
                    pass
                elif word not in self.keywords and line.startswith('var'):
                    pass
                elif word not in self.keywords and word in self.specialchars:
                    pass
                elif word==' ' or word=='':
                    pass
                else:
                    Error("GrammarError",f"Bad grammar: '{word}'\n{' '*18}{'~'*len(word)}\n{' '*18}^",self.ln,self.wn,self.__file__)
try:
    run=sys.argv[1]
except IndexError:
    print('Copyright (c) 2020 Bare.\nAll Rights Reserved.\n\n')
    while True:
        command=input(">>> ")
        j=open('stdin','w+').write(command)
        eva=Evaluator('stdin')
        eva.run('stdin')
        os.remove('stdin')
        
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
