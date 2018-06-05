# 在一般领域，对正整数n，如果用2到 n 开根 之间的所有整数去除，均无法整除，则n为质数。
# 质数大于等于2 不能被它本身和1以外的数整除
# import math
from math import sqrt
#编写一个函数isprime(x)，判断x是否为素数，如果是，返回TRUE，否则返回false
def isprime(x):
    flag = False
    for i in range(2,int(sqrt(x)+1)):
        if x%i == 0:
            return False
    return True

print(isprime(6))
#编写一个函数prime_m2n(m,n),返回从m开始，到n结束范围内的质数，返回这些质数的列表，并在主程序中打印
#如 L = prime_m2n(5,10) 打印出 [5,7]

def prime_m2n(m,n):
    prime_list = []
    for x in range(m,n+1):
        if isprime(x):
            prime_list.append(x)

    print(prime_list)
prime_m2n(1,47)
#编写一个函数primes(m)，打印出1-m范围内所有的素数
def primes(m):
    prime_list = []
    for x in range(1,m+1):
        if isprime(x):
            prime_list.append(x)

    print(prime_list)

primes(100)

#使用生成器生成一个素数列表
def generatorPrimes(begin, stop):
    '使用生成器生成一个素数列表'
    for x in range(begin,stop+1):
        if(isprime(x)):
            yield x


l=[x for x in generatorPrimes(10,20)]
print(l)