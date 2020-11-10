import pickle,sys
try:
    a=sys.argv[1]
    fs=open(a,'r')
    fsr=fs.read()
    a26=''
    class Compiler:
        def __init__(self):
            a1=fsr.replace('a','111111---')
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
    def Compile():
        atomc=Compiler()
        print("Initializing compiler...")
        bytsc=atomc.get()
        with open(f'{a[:-3]}.batom','wb') as f:
            pickle.dump(bytsc,f,protocol=2)
        print(f"Finished compiling '{a}'!\nPath:\n    {a[:-3]}.batom")
    Compile()
except IndexError:
    print("Syntax: [File]")
