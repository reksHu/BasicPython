#函数作为函数的返回值
# 练习:编写一个函数，带op参数，def get_operation(op):
# 此函数在传入字符串'Add',返回一个加操作的函数
# def myadd(x,y): return:x+y
# 传入一个字符串'Multipy',返回乘操作的函数
# def mymul(x,y):return x*y
# 在主函数中程序如下:
# a =  int(input("the first num:"))
# b =  int(input("the second num:"))
# operation =  input('operation plz (Add/Multipy):')
# fn = get_operation(operation)
# print("result:",fn(a,b))

def get_operation(op):
    def myadd(x,y):
        return x+y

    def mymul(x,y):
        return  x*y

    if op == "Add":
        return myadd
    if op == "Multipy":
        return mymul

while True:
    a = int(input("the first num:"))
    b = int(input("the second num:"))
    operation = input('operation plz (Add/Multipy):')
    fn = get_operation(operation)
    result = fn(a,b)
    print("result:",result)
