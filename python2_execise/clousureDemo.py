#闭包：将组成函数的语句和这些语句的执行环境打包在一起时，得到的对象称为闭包。
#如果一个内嵌函数访问外部作用域的变量，则这个函数就是闭包
def make_power(x):
    def fn(arg):
        return  arg**x
    return fn

f=make_power(2)
result = f(5)
print(result)  # 5**2

f =  make_power(3)
result = f(5) # 5**3
print(result)

f =  make_power(4)
result = f(5) # 5**3
print(result)