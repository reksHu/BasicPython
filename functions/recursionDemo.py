#递归函数,实现阶乘
def myfac(n):
    print(n)
    if n==1:
        return 1
    return n * myfac(n-1)



print("5!=" ,myfac(5))