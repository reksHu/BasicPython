# 编写一个不定长的minmax函数，返回参数的最大值和最小值（形成元组，最小值在前，最大值在后）
# 调用此函数，得到最大值和最小值

def minandmax(a,b,*args):
    print(a,b,args)
    maxresult=max(a,b)
    print(maxresult)
    maxresult =max(maxresult, max(args))
    print(maxresult)
    minresult=min(a,b)
    minresult = min(minresult,min(args))
    print(minresult)
    resultTuple =(minresult,maxresult)
    print(resultTuple)
    return resultTuple
    # listresult.append(list(args))
    # listresult.sort(reverse=True)


x,y = minandmax(5,1,100,3)
print(x,y)