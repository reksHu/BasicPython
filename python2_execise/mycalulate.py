# 1.给出一个数n，写一个函数来计算1+2+3+....的和
# print(mysum(100)) #5050

def newSum(n):
    result = 0
    for x in range(1,n+1):
        result +=x
    print(result)
    return newSum

# 2.给出一个数n,写一个函数计算n!
# n!=1*2*3*4****
def newMulp(n):
    result=1
    for x in range(1,n+1):
        result *=x
    print(result)
    return  newMulp
# 3.给出一个数n，写一个函数计算1+2**2+3**3 +..的和.
def mypower(n):
    return pow(n,n)

mapresult = map(mypower,range(1,10))
for x in mapresult:
    print(x,end=' ')

# print(newMulp)
# mysum = newSum
# mysum(100)
# myMul=newMulp
# myMul(5)

print("#"*20)
result = map((lambda x:pow(x,x)),range(1,10))
for x in result:
    print(x,end=' ')



