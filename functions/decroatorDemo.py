def decorator(fn):
    print('this is decorator function,return fn')
    return fn #必须返回函数引用,可以使lambda表达式

@decorator #装饰器函数， @装饰函数 等用于  myfun = decorator(myfun)
def myfun():
    print("main function")

myfun()

def money_service(fn):
    def message(name,account):
        print("welcome ", name," please stay in line.")
        fn(name,account)
        print("thanks for you cooperation. you saved $",account ," successfully")
    return message

@money_service
def saveMoney(name, account):
    print(name, " saved $",account)

saveMoney("Rex",1000000) #等价于下面函数
# service = money_service(saveMoney)
# print(service("rex",1000000))
