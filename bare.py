import os,sys,webbrowser,requests,pickle,tempfile,re,random,configparser,subprocess
from tkinter import font
goodGrammar=True
ptf=os.getcwd()
class Error:
    def __init__(self,name,details,ln,wn,fn):
        global goodGrammar
        if goodGrammar==False:
            print("\nDuring this error, another error occurred:\n")
        print("Error (Most recent is shown last):")
        print(f"  File '<{fn}>',")
        try:
            if ln.startswith('lift'):
                print(f"    Line '<lift>', word {wn}:")
            else:
                print(f"    Line {ln}, word {wn}:")
        except AttributeError:
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
DIGITS='0123456789'
ERRORS=['InvalidVariableError','UnknownFileError','ConnectionError','URLError','EmptyFunctionError','SyntaxError','UnopenFileError','SetCursorError','InvalidArgumentError','GrammarError','LiftingError','EquationError']
OPERATORS='+-*x/%()'
SPECIAL_CHARS=' .'
BARE_CHARS='$|'
OTHER_CHARS='\\'
ASCII="""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz[\\]^_`{|}~ \n"""
BUILT_IN_ATOMS=['time','system','bagui','os']
class Evaluator:
    def __init__(self, file):
        self.keywords=['say','ask','hyperlink','readout','say-previously-read','__root__','__name__','__package__','__doc__','delete','__keywords__','get-html','make','use','__system_arguments__','__change_window_title__','start','open','write','close','write-previously-read','read','if','default:','__get_keywords__','read-current','set-cursor','compile_atom','compile','var','__change_window_title_WE__','nothing','delete-directory','get','new-window','loop','add-text','add-inputfield','configure','add-space','errorize','lift','equation','wait','exit','add-button','forget','destroy-window','disable','enable','change-directory','get-response']
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
        self.variables=[]
        self.guisettings=['background-color','foreground-color','text']
    def RunKey(self,key,v):
        if not "'" in v and not '"' in v:
            try:
                if v!=' ' and v!='':
                    exec(key)
                else:
                    pass
            except:
                if not v in self.variables:
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
                        v=line[10:]
                        self.RunKey(f"try:\n    webbrowser.open(self.{v})\nexcept ConnectionError:\n    Error('ConnectionError',f\"Link '{v}' may not start with 'http' or 'https', please include this. If your link is correct, check if you are connected to the internet.\\n{' '*10}{'~'*len(v)}\\n{' '*10}\",self.ln,self.wn,self.__file__)",v)
                    elif word=='readout':
                        v=line[8:]
                        self.RunKey(f"try:\n    f=open(self.{v},'r')\n    self.r=f.read()\n    print(self.r)\nexcept FileNotFoundError:\n    Error(\"InvalidFileError\",f\"Could not find file '{v}'. Have you spelled it right?\\n{' '*25}{'~'*len(v)}\\n{' '*25}^\",self.ln,self.wn,self.__file__)",v)
                    elif word=='say-previously-read':
                        if self.r!=None:
                            print(self.r)
                        elif self.read!=None:
                            print(self.read)
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
                        built_in=False
                        if '-> ' in r:
                            v2=r.split(' -> ')
                            for v1 in v2:
                                if v1.startswith('[') and v1.endswith(']'):
                                    v1=v1[1:][:-1]
                                    if v1=='':
                                        p=os.getcwd()
                                    else:
                                        p=v1
                                else:
                                    vt=v1[1:][:-1]
                                    if vt in BUILT_IN_ATOMS:
                                        built_in=True
                                        complete=False
                                        if vt=='time':
                                            import time
                                            self.threading_time=time.thread_time()
                                            self.threading_nano=time.thread_time_ns()
                                            self.monotonic=time.monotonic()
                                            self.monotonic_nano=time.monotonic_ns()
                                            self.performance=time.perf_counter()
                                            self.performance_nano=time.perf_counter_ns()
                                            self.process_time=time.process_time()
                                            self.process_nano=time.process_time_ns()
                                            self.time=time.time()
                                            self.time_nano=time.time_ns()
                                            complete=True
                                        elif vt=='system':
                                            self.system_argv=sys.argv
                                            self.byteorder=sys.byteorder
                                            self.builtin_atom_names=BUILT_IN_ATOMS
                                            self.copyright='Copyright (c) 2020 Bare.\nAll Rights Reserved.'
                                            self.executable='C:\\Program Files (x86)\\Bare\\bare.exe'
                                            self.allocated_blocks=sys.getallocatedblocks()
                                            complete=True
                                        elif vt=='bagui':
                                            from functools import partial
                                            exec('from tkinter import *')
                                            complete=True
                                        elif vt=='os':
                                            self.os_name=os.name
                                            self.current_directory=os.getcwd()
                                            complete=True
                                        else:
                                            pass
                                        if complete==True:
                                            self.imports.append(vt)
                        if built_in==False:
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
                        cu='\x1b[1A'
                        dl='\x1b[2K'
                        n=(os.path.splitext(nr))[0]
                        subprocess.call(f"title {n}",shell=True)
                        sys.stdout.write(cu)
                        sys.stdout.write(dl)
                    elif word=='__change_window_title_WE__':
                        nr=sys.argv[1]
                        cu='\x1b[1A'
                        dl='\x1b[2K'
                        subprocess.call(f"title {nr}",shell=True)
                        sys.stdout.write(cu)
                        sys.stdout.write(dl)
                    elif word=='open':
                        v=line[5:][1:][:-1]
                        self.openfile=open(v,'w+')
                    elif word=='write':
                        v=line[6:][1:][:-1]
                        self.openfile.write(v)
                    elif word=='close':
                        self.openfile.close()
                    elif word=='read':
                        v=line[5:][1:][:-1]
                        h=open(v,'r')
                        self.read=h.read()
                    elif word=='read-current':
                        try:
                            self.read=self.openfile.read()
                        except AttributeError:
                            Error("UnopenFileError",f"Could not execute keyword read-current, because you do not have a file open.",self.ln,self.wn,self.__file__)
                    elif word=='set-cursor':
                        try:
                            v=int(line[11:][1:][:-1])
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
                        print(self.keywords)
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
                        con=vlist[1]
                        va=vlist[0]
                        if con.startswith("'") and con.endswith("'") or con.startswith('"') and con.endswith('"'):
                            exec(f'self.{va}={con}')
                        else:
                            exec(f'self.{va}=self.{con}')
                        self.registers.append(va)
                    elif word=='nothing':
                        pass
                    elif word=='__QUIT_EXIT__':
                        sys.exit()
                    elif word=='delete-directory':
                        v=line[17:]
                        self.RunKey(f'os.rmdir(self.{v})',v)
                    elif word=='get':
                        v=line[4:].split('=')
                        if len(v)>4:
                            v2=v[1]
                            n=v[0]
                            exec(f'self.{n}=input({v2})')
                        else:
                            n=v[0]
                            exec(f'self.{n}=input()')
                            self.registers.append(n)
                            self.variables.append(n)
                    elif word=='new-window':
                        v=line[11:][1:][:-1]
                        exec(f'self.{v}=Tk()\nself.{v}.title("ba")\nself.{v}.geometry("500x350")')
                        self.registers.append(v)
                    elif word=='loop':
                        v=line[5:][1:][:-1]
                        exec(f'self.{v}.mainloop()')
                    elif word=='add-text':
                        v=line[9:].split(' ; ')
                        finaltxt=''
                        fgc=None
                        bgc=None
                        txt=None
                        tfont=None
                        fsize=0
                        fweight=''
                        ffont=''
                        nosize=False
                        noweight=False
                        label=None
                        labelnum=random.randint(0,30000)
                        master=f'self.{v[0][1:][:-1]}'
                        for m in v:
                            if m.startswith('foreground-color'):
                                fgc=m[17:]
                            elif m.startswith('background-color'):
                                bgc=m[17:]
                            elif m.startswith('text'):
                                txt=m[5:]
                            elif m.startswith('font-size'):
                                fsize=m[10:]
                            elif m.startswith('font-weight'):
                                fweight=m[12:]
                            elif m.startswith('font'):
                                tfont=m[5:]
                            elif m.startswith('label'):
                                label=m[6:][1:][:-1]
                        if fgc!=None:
                            finaltxt+=f',fg={fgc}'
                        if bgc!=None:
                            finaltxt+=f',bg={bgc}'
                        if tfont!=None and fsize!=0 and fweight!='':
                            exec(f"self.{label}font=font.Font(family=tfont[1:][:-1], size=fsize, weight=fweight[1:][:-1])")
                            ffont=f'self.{label}["font"]=self.{label}font'
                        if txt!=None:
                            finaltxt+=f',text={txt}'
                        if label==None:
                            label=f'text{labelnum}'
                        exec(f'self.{label}=Label({master}{finaltxt})\n{ffont}\nself.{label}.pack()')
                        tfont=''
                        fsize=0
                        fweight=''
                    elif word=='forget':
                        v=line[7:][1:][:-1]
                        exec(f'self.{v}.pack_forget()')
                    elif word=='disable':
                        v=line[8:][:-1][1:]
                        exec(f'self.{v}["state"]="disabled"')
                    elif word=='enable':
                        v=line[7:][:-1][1:]
                        exec(f'self.{v}["state"]="enabled"')
                    elif word=='add-inputfield':
                        v=line[15:].split(' ; ')
                        finalinp=''
                        fgc=None
                        bgc=None
                        txt=None
                        master=f'self.{v[0][1:][:-1]}'
                        label=''
                        tfont=None
                        fsize=0
                        ffont=None
                        entrynum=random.randint(0,30000)
                        for m in v:
                            if m.startswith('foreground-color'):
                                fgc=m[17:]
                            elif m.startswith('background-color'):
                                bgc=m[17:]
                            elif m.startswith('text'):
                                txt=m[5:]
                            elif m.startswith('label'):
                                label=m[6:][:-1][1:]
                            elif m.startswith('font-size'):
                                fsize=m[10:]
                            elif m.startswith('font-weight'):
                                fweight=m[12:]
                            elif m.startswith('font'):
                                tfont=m[5:]
                        if fgc!=None:
                            finalinp+=f',fg={fgc}'
                        if bgc!=None:
                            finalinp+=f',bg={bgc}'
                        if label=='':
                            label=f'field{entrynum}'
                        if txt!=None:
                            insert=f'self.{label}.insert(0,{txt})'
                        if tfont!=None and fsize!=0 and fweight!='':
                            exec(f"self.{label}font=font.Font(family=tfont[1:][:-1], size=fsize, weight=fweight[1:][:-1])")
                            ffont=f'self.{label}["font"]=self.{label}font'
                        exec(f'self.{label}=Entry({master}{finalinp})\n{ffont}\n{insert}\nself.{label}.pack()')
                        tfont=''
                        fsize=0
                        fweight=''
                    elif word=='configure':
                        v=line[9:].split(' ; ')
                        finalcon=''
                        bgc=None
                        fgc=None
                        wid=None
                        hei=None
                        ful=False
                        titl=None
                        acon=''
                        wcon=''
                        hcon=''
                        titlcmd=''
                        master=f'self.{v[0][2:][:-1]}'
                        entrynum=random.randint(0,30000)
                        for m in v:
                            if m.startswith('background-color'):
                                bgc=m[17:]
                            if m.startswith('width'):
                                wid=m[6:]
                            if m.startswith('height'):
                                hei=m[7:]
                            if m.startswith('fullscreen'):
                                ful=bool(m[11:])
                            if m.startswith('title'):
                                titl=m[6:]
                        if titl!=None:
                            titlcmd=f'{master}.title({titl})'
                        if bgc!=None:
                            finalcon+=f'background={bgc},'
                        if wid!=None:
                            wcon=wid
                        if hei!=None:
                            hcon=hei
                        if finalcon.endswith(','):
                            finalcon=finalcon[:-1]
                        if ful==True:
                            acon=f'{master}.attributes("-fullscreen", True)'
                        if wcon!='' and hcon!='':
                            exec(f'{master}.configure({finalcon})\n{acon}\n{master}.geometry("{wcon}x{hcon}")\n{titlcmd}')
                        else:
                            exec(f'{master}.configure({finalcon})\n{acon}\n{titlcmd}')
                    elif word=='add-button':
                        if 'bagui' in self.imports:
                            pass
                        else:
                            print("Bagui: Atom 'bagui' needs to be used. To do that, copy this line of code:\nuse <bagui> -> [built-in]")
                            return
                        v=line[11:].split(' ; ')
                        finalbtn=''
                        fgc=None
                        bgc=None
                        txt=None
                        brd=None
                        wdt=None
                        hei=None
                        cmd=None
                        label=''
                        master=f'self.{v[0][1:][:-1]}'
                        btnnum=random.randint(0,30000)
                        for m in v:
                            if m.startswith('foreground-color'):
                                fgc=m[17:]
                            elif m.startswith('background-color'):
                                bgc=m[17:]
                            elif m.startswith('text'):
                                txt=m[5:]
                            elif m.startswith('border'):
                                brd=m[7:]
                            elif m.startswith('width'):
                                wdt=m[6:]
                            elif m.startswith('height'):
                                hei=m[7:]
                            elif m.startswith('command'):
                                cmd=m[8:]
                            elif m.startswith('label'):
                                label=m[6:][1:][:-1]
                        if fgc!=None:
                            finalbtn+=f',fg={fgc}'
                        if bgc!=None:
                            finalbtn+=f',bg={bgc}'
                        if txt!=None:
                            finalbtn+=f',text={txt}'
                        if brd!=None:
                            finalbtn+=f',border={brd}'
                        if wdt!=None:
                            finalbtn+=f',width={wdt}'
                        if hei!=None:
                            finalbtn+=f',height={hei}'
                        if label=='':
                            label=f'button{btnnum}'
                        if cmd!=None:
                            finalbtn+=f',command=partial(self.runFunc,self.{cmd[1:]},cmd)'
                        exec(f'self.{label}=Button({master}{finalbtn})\nself.{label}.pack()')
                    elif word=='add-space':
                        v=line[10:].split(' ; ')
                        master=f'self.{v[0][:-1][1:]}'
                        empnum=random.randint(0,30000)
                        exec(f'emptylabel{empnum}=Label({master},bg="{v[1][:-1][1:]}")\nemptylabel{empnum}.pack()')
                    elif word=='destroy-window':
                        v=line[14:]
                        self.RunKey(f'self.{v}.destroy()',v)
                    elif word=='errorize':
                        v=line[9:]
                        self.RunKey(f'ERRORS.append(self.{v})',v)
                    elif word=='lift':
                        v=line[5:].split(': ')
                        n=v[0].replace("'",'').replace('"','')
                        e=v[1].replace("'",'').replace('"','')
                        if n in ERRORS:
                            Error(n,e,line,self.ln,self.__file__)
                        else:
                            Error("LiftingError",f"Could not lift '{v[0][:-1][1:]}', because it is not a valid error. Have you used the keyword 'errorize'?\n{' '*20}{'~'*(len(v[0])-2)}\n{' '*20}^",self.ln,self.wn,self.__file__)
                    elif word=='equation':
                        v=line[9:].split('=')
                        n=v[0]
                        s=v[1].replace('x','*')
                        for i in s:
                            if i in OPERATORS or i in DIGITS or i in SPECIAL_CHARS:
                                pass
                            else:
                                Error("EquationError",f"Could not equate '{s}', because '{i}' is not an operator / digit.\n{' '*22}{'~'*(len(s)-2)}\n{' '*22}^",self.ln,self.wn,self.__file__)
                                return
                        exec(f'self.{n}={s}')
                        self.registers.append(n)
                    elif word=='wait':
                        v=line[5:]
                        if 'time' in self.imports:
                            time.sleep(int(v))
                        else:
                            pass
                    elif word=='exit':
                        if 'system' in self.imports:
                            sys.exit()
                        else:
                            pass
                    elif word=='change-directory':
                        v=line[17:]
                        if 'os' in self.imports:
                            exec(f'os.chdir({v})')
                        else:
                            pass
                    elif word=='get-response':
                        v=line[13:]
                        vlist=v.split('=')
                        con=vlist[1]
                        va=vlist[0][1:][:-1]
                        exec(f'self.{con}=self.{va}.get()')
                        self.registers.append(va)
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
                elif not word in self.keywords and word.startswith('[') and word.endswith(']'):
                    pass
                elif word not in self.keywords and line.startswith('var'):
                    pass
                elif word not in self.keywords and line.startswith('equation'):
                    pass
                elif word not in self.keywords and line.startswith('get-response'):
                    pass
                elif word not in self.keywords and word in self.specialchars:
                    pass
                elif word==' ' or word=='':
                    pass
                else:
                    curbadgrammar=False
                    for w in self.guisettings:
                        if word.startswith(w):
                            pass
                        else:
                            for i in word:
                                if i in DIGITS or i in OPERATORS or i in SPECIAL_CHARS or i in BARE_CHARS or i in OTHER_CHARS:
                                    pass
                                elif word in dir(self):
                                    pass
                                else:
                                    curbadgrammar=True
                    if curbadgrammar==True:
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
                        v=line[10:]
                        self.RunKey(f"try:\n    webbrowser.open(self.{v})\nexcept ConnectionError:\n    Error('ConnectionError',f\"Link '{v}' may not start with 'http' or 'https', please include this. If your link is correct, check if you are connected to the internet.\\n{' '*10}{'~'*len(v)}\\n{' '*10}\",self.ln,self.wn,self.__file__)",v)
                    elif word=='readout':
                        v=line[8:]
                        self.RunKey(f"try:\n    f=open(self.{v},'r')\n    self.r=f.read()\n    print(self.r)\nexcept FileNotFoundError:\n    Error(\"InvalidFileError\",f\"Could not find file '{v}'. Have you spelled it right?\\n{' '*25}{'~'*len(v)}\\n{' '*25}^\",self.ln,self.wn,self.__file__)",v)
                    elif word=='say-previously-read':
                        if self.r!=None:
                            print(self.r)
                        elif self.read!=None:
                            print(self.read)
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
                        built_in=False
                        if '-> ' in r:
                            v2=r.split(' -> ')
                            for v1 in v2:
                                if v1.startswith('[') and v1.endswith(']'):
                                    v1=v1[1:][:-1]
                                    if v1=='':
                                        p=os.getcwd()
                                    else:
                                        p=v1
                                else:
                                    vt=v1[1:][:-1]
                                    if vt in BUILT_IN_ATOMS:
                                        built_in=True
                                        complete=False
                                        if vt=='time':
                                            import time
                                            self.threading_time=time.thread_time()
                                            self.threading_nano=time.thread_time_ns()
                                            self.monotonic=time.monotonic()
                                            self.monotonic_nano=time.monotonic_ns()
                                            self.performance=time.perf_counter()
                                            self.performance_nano=time.perf_counter_ns()
                                            self.process_time=time.process_time()
                                            self.process_nano=time.process_time_ns()
                                            self.time=time.time()
                                            self.time_nano=time.time_ns()
                                            complete=True
                                        elif vt=='system':
                                            self.system_argv=sys.argv
                                            self.byteorder=sys.byteorder
                                            self.builtin_atom_names=BUILT_IN_ATOMS
                                            self.copyright='Copyright (c) 2020 Bare.\nAll Rights Reserved.'
                                            self.executable='C:\\Program Files (x86)\\Bare\\bare.exe'
                                            self.allocated_blocks=sys.getallocatedblocks()
                                            complete=True
                                        elif vt=='bagui':
                                            from functools import partial
                                            exec('from tkinter import *')
                                            complete=True
                                        elif vt=='os':
                                            self.os_name=os.name
                                            self.current_directory=os.getcwd()
                                            complete=True
                                        else:
                                            pass
                                        if complete==True:
                                            self.imports.append(vt)
                        if built_in==False:
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
                        cu='\x1b[1A'
                        dl='\x1b[2K'
                        n=(os.path.splitext(nr))[0]
                        subprocess.call(f"title {n}",shell=True)
                        sys.stdout.write(cu)
                        sys.stdout.write(dl)
                    elif word=='__change_window_title_WE__':
                        nr=sys.argv[1]
                        cu='\x1b[1A'
                        dl='\x1b[2K'
                        subprocess.call(f"title {nr}",shell=True)
                        sys.stdout.write(cu)
                        sys.stdout.write(dl)
                    elif word=='open':
                        v=line[5:][1:][:-1]
                        self.openfile=open(v,'w+')
                    elif word=='write':
                        v=line[6:][1:][:-1]
                        self.openfile.write(v)
                    elif word=='close':
                        self.openfile.close()
                    elif word=='read':
                        v=line[5:][1:][:-1]
                        h=open(v,'r')
                        self.read=h.read()
                    elif word=='read-current':
                        try:
                            self.read=self.openfile.read()
                        except AttributeError:
                            Error("UnopenFileError",f"Could not execute keyword read-current, because you do not have a file open.",self.ln,self.wn,self.__file__)
                    elif word=='set-cursor':
                        try:
                            v=int(line[11:][1:][:-1])
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
                        print(self.keywords)
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
                        con=vlist[1]
                        va=vlist[0]
                        if con.startswith("'") and con.endswith("'") or con.startswith('"') and con.endswith('"'):
                            exec(f'self.{va}={con}')
                        else:
                            exec(f'self.{va}=self.{con}')
                        self.registers.append(va)
                    elif word=='nothing':
                        pass
                    elif word=='__QUIT_EXIT__':
                        sys.exit()
                    elif word=='delete-directory':
                        v=line[17:]
                        self.RunKey(f'os.rmdir(self.{v})',v)
                    elif word=='get':
                        v=line[4:].split('=')
                        if len(v)>4:
                            v2=v[1]
                            n=v[0]
                            exec(f'self.{n}=input({v2})')
                        else:
                            n=v[0]
                            exec(f'self.{n}=input()')
                            self.registers.append(n)
                            self.variables.append(n)
                    elif word=='new-window':
                        v=line[11:][1:][:-1]
                        exec(f'self.{v}=Tk()\nself.{v}.title("ba")\nself.{v}.geometry("500x350")')
                        self.registers.append(v)
                    elif word=='loop':
                        v=line[5:][1:][:-1]
                        exec(f'self.{v}.mainloop()')
                    elif word=='add-text':
                        v=line[9:].split(' ; ')
                        finaltxt=''
                        fgc=None
                        bgc=None
                        txt=None
                        tfont=None
                        fsize=0
                        fweight=''
                        ffont=''
                        nosize=False
                        noweight=False
                        label=None
                        labelnum=random.randint(0,30000)
                        master=f'self.{v[0][1:][:-1]}'
                        for m in v:
                            if m.startswith('foreground-color'):
                                fgc=m[17:]
                            elif m.startswith('background-color'):
                                bgc=m[17:]
                            elif m.startswith('text'):
                                txt=m[5:]
                            elif m.startswith('font-size'):
                                fsize=m[10:]
                            elif m.startswith('font-weight'):
                                fweight=m[12:]
                            elif m.startswith('font'):
                                tfont=m[5:]
                            elif m.startswith('label'):
                                label=m[6:][1:][:-1]
                        if fgc!=None:
                            finaltxt+=f',fg={fgc}'
                        if bgc!=None:
                            finaltxt+=f',bg={bgc}'
                        if tfont!=None and fsize!=0 and fweight!='':
                            exec(f"self.{label}font=font.Font(family=tfont[1:][:-1], size=fsize, weight=fweight[1:][:-1])")
                            ffont=f'self.{label}["font"]=self.{label}font'
                        if txt!=None:
                            finaltxt+=f',text={txt}'
                        if label==None:
                            label=f'text{labelnum}'
                        exec(f'self.{label}=Label({master}{finaltxt})\n{ffont}\nself.{label}.pack()')
                        tfont=''
                        fsize=0
                        fweight=''
                    elif word=='forget':
                        v=line[7:][1:][:-1]
                        exec(f'self.{v}.pack_forget()')
                    elif word=='disable':
                        v=line[8:][:-1][1:]
                        exec(f'self.{v}["state"]="disabled"')
                    elif word=='enable':
                        v=line[7:][:-1][1:]
                        exec(f'self.{v}["state"]="enabled"')
                    elif word=='add-inputfield':
                        v=line[15:].split(' ; ')
                        finalinp=''
                        fgc=None
                        bgc=None
                        txt=None
                        master=f'self.{v[0][1:][:-1]}'
                        label=''
                        tfont=None
                        fsize=0
                        ffont=None
                        entrynum=random.randint(0,30000)
                        for m in v:
                            if m.startswith('foreground-color'):
                                fgc=m[17:]
                            elif m.startswith('background-color'):
                                bgc=m[17:]
                            elif m.startswith('text'):
                                txt=m[5:]
                            elif m.startswith('label'):
                                label=m[6:][:-1][1:]
                            elif m.startswith('font-size'):
                                fsize=m[10:]
                            elif m.startswith('font-weight'):
                                fweight=m[12:]
                            elif m.startswith('font'):
                                tfont=m[5:]
                        if fgc!=None:
                            finalinp+=f',fg={fgc}'
                        if bgc!=None:
                            finalinp+=f',bg={bgc}'
                        if label=='':
                            label=f'field{entrynum}'
                        if txt!=None:
                            insert=f'self.{label}.insert(0,{txt})'
                        if tfont!=None and fsize!=0 and fweight!='':
                            exec(f"self.{label}font=font.Font(family=tfont[1:][:-1], size=fsize, weight=fweight[1:][:-1])")
                            ffont=f'self.{label}["font"]=self.{label}font'
                        exec(f'self.{label}=Entry({master}{finalinp})\n{ffont}\n{insert}\nself.{label}.pack()')
                        tfont=''
                        fsize=0
                        fweight=''
                    elif word=='configure':
                        v=line[9:].split(' ; ')
                        finalcon=''
                        bgc=None
                        fgc=None
                        wid=None
                        hei=None
                        ful=False
                        titl=None
                        acon=''
                        wcon=''
                        hcon=''
                        titlcmd=''
                        master=f'self.{v[0][2:][:-1]}'
                        entrynum=random.randint(0,30000)
                        for m in v:
                            if m.startswith('background-color'):
                                bgc=m[17:]
                            if m.startswith('width'):
                                wid=m[6:]
                            if m.startswith('height'):
                                hei=m[7:]
                            if m.startswith('fullscreen'):
                                ful=bool(m[11:])
                            if m.startswith('title'):
                                titl=m[6:]
                        if titl!=None:
                            titlcmd=f'{master}.title({titl})'
                        if bgc!=None:
                            finalcon+=f'background={bgc},'
                        if wid!=None:
                            wcon=wid
                        if hei!=None:
                            hcon=hei
                        if finalcon.endswith(','):
                            finalcon=finalcon[:-1]
                        if ful==True:
                            acon=f'{master}.attributes("-fullscreen", True)'
                        if wcon!='' and hcon!='':
                            exec(f'{master}.configure({finalcon})\n{acon}\n{master}.geometry("{wcon}x{hcon}")\n{titlcmd}')
                        else:
                            exec(f'{master}.configure({finalcon})\n{acon}\n{titlcmd}')
                    elif word=='add-button':
                        if 'bagui' in self.imports:
                            pass
                        else:
                            print("Bagui: Atom 'bagui' needs to be used. To do that, copy this line of code:\nuse <bagui> -> [built-in]")
                            return
                        v=line[11:].split(' ; ')
                        finalbtn=''
                        fgc=None
                        bgc=None
                        txt=None
                        brd=None
                        wdt=None
                        hei=None
                        cmd=None
                        label=''
                        master=f'self.{v[0][1:][:-1]}'
                        btnnum=random.randint(0,30000)
                        for m in v:
                            if m.startswith('foreground-color'):
                                fgc=m[17:]
                            elif m.startswith('background-color'):
                                bgc=m[17:]
                            elif m.startswith('text'):
                                txt=m[5:]
                            elif m.startswith('border'):
                                brd=m[7:]
                            elif m.startswith('width'):
                                wdt=m[6:]
                            elif m.startswith('height'):
                                hei=m[7:]
                            elif m.startswith('command'):
                                cmd=m[8:]
                            elif m.startswith('label'):
                                label=m[6:][1:][:-1]
                        if fgc!=None:
                            finalbtn+=f',fg={fgc}'
                        if bgc!=None:
                            finalbtn+=f',bg={bgc}'
                        if txt!=None:
                            finalbtn+=f',text={txt}'
                        if brd!=None:
                            finalbtn+=f',border={brd}'
                        if wdt!=None:
                            finalbtn+=f',width={wdt}'
                        if hei!=None:
                            finalbtn+=f',height={hei}'
                        if label=='':
                            label=f'button{btnnum}'
                        if cmd!=None:
                            finalbtn+=f',command=partial(self.runFunc,self.{cmd[1:]},cmd)'
                        exec(f'self.{label}=Button({master}{finalbtn})\nself.{label}.pack()')
                    elif word=='add-space':
                        v=line[10:].split(' ; ')
                        master=f'self.{v[0][:-1][1:]}'
                        empnum=random.randint(0,30000)
                        exec(f'emptylabel{empnum}=Label({master},bg="{v[1][:-1][1:]}")\nemptylabel{empnum}.pack()')
                    elif word=='destroy-window':
                        v=line[14:]
                        self.RunKey(f'self.{v}.destroy()',v)
                    elif word=='errorize':
                        v=line[9:]
                        self.RunKey(f'ERRORS.append(self.{v})',v)
                    elif word=='lift':
                        v=line[5:].split(': ')
                        n=v[0].replace("'",'').replace('"','')
                        e=v[1].replace("'",'').replace('"','')
                        if n in ERRORS:
                            Error(n,e,line,self.ln,self.__file__)
                        else:
                            Error("LiftingError",f"Could not lift '{v[0][:-1][1:]}', because it is not a valid error. Have you used the keyword 'errorize'?\n{' '*20}{'~'*(len(v[0])-2)}\n{' '*20}^",self.ln,self.wn,self.__file__)
                    elif word=='equation':
                        v=line[9:].split('=')
                        n=v[0]
                        s=v[1].replace('x','*')
                        for i in s:
                            if i in OPERATORS or i in DIGITS or i in SPECIAL_CHARS:
                                pass
                            else:
                                Error("EquationError",f"Could not equate '{s}', because '{i}' is not an operator / digit.\n{' '*22}{'~'*(len(s)-2)}\n{' '*22}^",self.ln,self.wn,self.__file__)
                                return
                        exec(f'self.{n}={s}')
                        self.registers.append(n)
                    elif word=='wait':
                        v=line[5:]
                        if 'time' in self.imports:
                            time.sleep(int(v))
                        else:
                            pass
                    elif word=='exit':
                        if 'system' in self.imports:
                            sys.exit()
                        else:
                            pass
                    elif word=='change-directory':
                        v=line[17:]
                        if 'os' in self.imports:
                            exec(f'os.chdir({v})')
                        else:
                            pass
                    elif word=='get-response':
                        v=line[13:]
                        vlist=v.split('=')
                        con=vlist[1]
                        va=vlist[0][1:][:-1]
                        exec(f'self.{con}=self.{va}.get()')
                        self.registers.append(va)
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
                elif not word in self.keywords and word.startswith('[') and word.endswith(']'):
                    pass
                elif word not in self.keywords and line.startswith('var'):
                    pass
                elif word not in self.keywords and line.startswith('equation'):
                    pass
                elif word not in self.keywords and line.startswith('get-response'):
                    pass
                elif word not in self.keywords and word in self.specialchars:
                    pass
                elif word==' ' or word=='':
                    pass
                else:
                    curbadgrammar=False
                    for w in self.guisettings:
                        if word.startswith(w):
                            pass
                        else:
                            for i in word:
                                if i in DIGITS or i in OPERATORS or i in SPECIAL_CHARS or i in BARE_CHARS or i in OTHER_CHARS:
                                    pass
                                elif word in dir(self):
                                    pass
                                else:
                                    curbadgrammar=True
                    if curbadgrammar==True:
                        Error("GrammarError",f"Bad grammar: '{word}'\n{' '*18}{'~'*len(word)}\n{' '*18}^",self.ln,self.wn,self.__file__)
    def MakeFunctions(self):
        exitfunc='make $exit: __QUIT_EXIT__'
        j=open('$init__bare.BaRT','w+')
        j.write(exitfunc)
        j.close()
        self.run('$init__bare.BaRT')
        os.remove('$init__bare.BaRT')
try:
    run=sys.argv[1]
except IndexError:
    print('Copyright (c) 2020 Bare.\nAll Rights Reserved.\n\n')
    while True:
        try:
            os.remove('$init__bare.BaRT')
            os.remove('$$exit.BaRT')
        except:
            pass
        command=input(">>> ")
        if os._exists('stdin'):
            j=open('stdin','a').write(command)
        else:
            j=open('stdin','w+').write(command)
        eva=Evaluator('stdin')
        eva.MakeFunctions()
        eva.run('stdin')
def decompile(content):
    content=content.replace('\61---','a')
    content=content.replace('\62---','b')
    content=content.replace('\63---','c')
    content=content.replace('\64---','d')
    content=content.replace('\65---','e')
    content=content.replace('\66---','f')
    content=content.replace('\67---','g')
    content=content.replace('\60---','h')
    content=content.replace('\0---','i')
    content=content.replace('\10---','j')
    content=content.replace('\11---','k')
    content=content.replace('\17---','l')
    content=content.replace('\13---','m')
    content=content.replace('\14---','n')
    content=content.replace('\16---','o')
    content=content.replace('\70---','p')
    content=content.replace('\71---','q')
    content=content.replace('\72---','r')
    content=content.replace('\73---','s')
    content=content.replace('\74---','t')
    content=content.replace('\75---','u')
    content=content.replace('\76---','v')
    content=content.replace('\77---','w')
    content=content.replace('\50---','x')
    content=content.replace('\51---','y')
    content=content.replace('\52---','z')
    return content
def RunCompiled():
    decompile(open(run,'r').read())
    FileRun=(os.path.splitext(run))[0]
    decomp=open(f'{FileRun}.ba','w+')
    decomp.write(decompile(open(run,'r').read()))
    decomp.close()
    ev=Evaluator(f'{FileRun}.ba')
    ev.MakeFunctions()
    ev.run(f'{FileRun}.ba')
    os.remove(f'{FileRun}.ba')
def RunNormal():
    ev=Evaluator(run)
    ev.MakeFunctions()
    ev.run(run)
def main():
    if run=='new':
        if len(sys.argv)<3:
            print("New file types:\n")
            print("    Command      Type")
            print("----------------------")
            print("    console      Console/Terminal Application (For backend applications, no GUI)")
            print("    window       Windowed Application (For front-end applications, with GUI)")
        else:
            type_=sys.argv[2]
            win_temp=''
            if len(sys.argv)==4:
                win_temp=sys.argv[3]
            print(f"Creating new file, type: {type_}")
            f=open('Application.ba','w+')
            if type_=='console':
                f.write('|| New Console application - generated with Bare')
            elif type_=='window' and win_temp=='':
                f.write("||  Imports / Uses\nuse <bagui> -> [built-in]\n\n|| Window Initialization\nnew-window 'root'\n\n|| Window - Start Looping Frames\nloop 'root'")
            elif type_=='window' and win_temp=='template':
                f.write("||  Imports / Uses\nuse <bagui> -> [built-in]\n\n|| Window Initialization\nnew-window 'root'\n\n|| Window Configuration\nconfigure 'root' ; background-color='#282828' ; title='Application'\n\n|| Add Widgets To Window\nadd-text 'root' ; label='Label_1' ; background-color='#282828' ; foreground-color='white' ; text='Test Application' ; font='Haettenschweiler' ; font-size=65 ; font-weight='normal'\nadd-space 'root' ; '#282828'\nadd-text 'root' ; label='Login' ; background-color='#282828' ; foreground-color='white' ; text='Login' ; font='Haettenschweiler' ; font-size=15 ; font-weight='normal'\nadd-space 'root' ; '#282828'\nadd-inputfield 'root' ; label='Username' ; text='Username'\nadd-inputfield 'root' ; label='Password' ; text='Password'\nmake $checklogin: get-response 'Username'=uname | get-response 'Password'=upass | say 'Username:' | say uname | say '\\\\n' | say 'Password:' | say upass\nadd-space 'root' ; '#282828'\nadd-button 'root' ; label='LoginButton' ; width=25 ; command=$checklogin ; text='Login' ; border=0\n\n|| Window - Start Looping Frames\nloop 'root'")
            else:
                print(f"Type '{type_}' does not exist.")
            f.close()
    else:
        compiled=False
        for char in open(run,'r').read():
            if char not in ASCII:
                compiled=True
        if compiled==True:
            RunCompiled()
        else:
            RunNormal()
main()
