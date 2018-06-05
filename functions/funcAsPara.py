#函数的引用作为函数的参数

def tab(x,y):
    return "|" + x.center(13) + "|" + y.center(13) +"|"

def toString(x,y):
    return str.format("name:{},age:{}",x,y)

def printFn(fn,x,y):
    print(fn(x,y))

printFn(tab,"abc","25")
printFn(toString,"abc","18")