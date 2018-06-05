#用函数式编程，计算出1-20阶乘的和
#1!+2!+3!....20!
def myfactorial(n):
    if n==1:
        return 1
    return n * myfactorial(n-1)

def factorialSum(result):
    print(result)


# method 1
# l=[]
# for x in range(1,10):
#     l.append(myfactorial(x))
# print(sum(l))


#method 2
factMap = map(myfactorial,range(1,5))
for x in factMap:print(x)
print(sum(factMap))

# help("__main__")
# print(list(factMap))
# print(list(l),sum(l))

