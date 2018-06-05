#可变参数类型
s = set()
def changedSet():
    s.add('a')

#不可变参数类型
t =(1,2,3)
def changedTuple(x):
    x[1]=2.2

# changedTuple(t)  #函数赋值出错
# print(t)

L = [1,2,3]
def fn2(x):
    #x.append(7)
    x=[4,5,6]
    x.append(8)

fn2(L)
print(L)



