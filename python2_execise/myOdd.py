# 写一个生成器函数myodd(x),传入一个终止值，可生成一个生成1,3,5,7,...x奇数的生成器
# 用for 语句打印出这些奇数

def myodd(x):
    mylist = range(1,x+1,2)
    for x in mylist:
        print('for in loop')
        yield x

oddit =myodd(100000000)
print(next(oddit))
print(next(oddit))
print(next(oddit))
# try:
#     while True:
#         print(next(oddit))
# except StopIteration as ex:
#     print("ended")