a=10
b=3
def fn(c,d):
    e=300
    print("locals:",locals()) #
    print("globals:",globals())  #including 'a':10,'b':3
    g = globals()
    print("file path:", g["__file__"])
    g['b'] = 350
fn(100,200)
print(b) # b = 350

x,y = 100,200
a= eval("x+y")
print(a) #300
local_scope={'x':5,'y':10}
a = eval('x+y',None,local_scope)
print(a) # 15
print("locals:", locals())
print("globals:", globals())