#1.全局变量如果要在函数内部赋值，则必须经过全局变量声明，否则被认为局部变量
f=100
def fn():
    # print(f) #运行错误，没有申明f.
    global f
    print(f)
fn()

#2.全局变量在函数内不经过声明就可以直接访问(前提是变量已经存在)
global f1
f1 = 200
def fn1():
    print(f1)
fn1()

#3.不能先申明局部变量，再用global声明为全局变量
# f2=300
# def fn2():
#     f2=400
#     global f2  #语法错误，global不能出现在变量声明之后.

#4.global 变量不能出现在列表里，for循环控制目标中，类定义，函数定义及import导入名中
def fn3(v):
    # global v  #错误，函数形参已经定义v，不能为v设置global

    global x
    for x in [1,2,3]:
        print("x=",x)
    def fn2_sub():
        print(x)
    fn2_sub()
fn3(1)
















