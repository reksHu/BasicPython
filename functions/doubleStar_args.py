def myfun(a, b, *, c): #c为命名关键字形参,*代表空一位
    print(a, b, c)

myfun(1, 2, c=3)
#myfun(1, 2) # myfun() missing 1 required keyword-only argument: 'c'

def myfun2(a,*args,b,c):  #b,c为命名关键字参数
    print(a,b,c,args)

myfun2(1,2,'a',b='b',c='c')

def myfun3(a,b,c,*args):
    print(a,b,c,args)

myfun3(1,2,3,4,5,6)

def myfun4(**args):
    print("the cout of parameters:",len(args),", Type:",type(args))
    for k,v in args.items():
        print("%s ---> %s" %(k,v))

myfun4(name="aaa",age="18",d=True)