#用递归方式计算1+2+3...n的和
def mysum(n):
    if n==1:
        return 1
    return n+mysum(n-1)

print("100=",mysum(10))

