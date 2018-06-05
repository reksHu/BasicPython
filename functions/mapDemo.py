def pow2(x):
    return x**2

mit = map(pow2,range(1,10))
# for x in mit:print(x)

#练习:生成一个迭代器，1*4,2*3,3*2,4*1
def arrayMul(x,y):
    print(x,"*",y,"=",end="")
    return x*y

resultMap = map(arrayMul,[1,2,3,4],[4,3,2,1])
for x in resultMap:print(x)

#生成第二个迭代器：1*2,1*3,1*4,2*3,2*4...  [1,2,3,4]
# def mynewArray(arg):