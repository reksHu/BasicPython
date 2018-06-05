#单层感知器
#假设平面上有三个点,(3,3),(4,3) 这两个点的标签为1,(1,1)这个点的标签为-1,构建神经网络分类。
#思路:要分类的数据是2维数据，所以只需要2个输入节点，我们可以把神经元的偏执值也设置成一个节点，这样我们需要3个输入节点
#输入的数据有3个(1,3,3),(1，4,3)，（1,1,1），数据对应的标签(1,1,-1),
#初始化权值w1,w2,w3,取-1到1的随机数，学习率(learning rate)设置为0.11，激活函数sign

import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1,3,3],
    [1,4,3],
    [1,1,1]
])

Y = np.array([1,1,-1])

W=(np.random.random(3)-0.5)*2

#learning rage
lr = 0.11
n = 0
output = 0

def update():
    global n,X,Y,W,lr,output
    n = n+1
    output = np.sign(np.dot(X,W.T))
    #权值改变
    W_changed =(lr *(Y-output.T).dot(X))/X.shape[0]
    W =W+W_changed



for i,x in enumerate(range(10000000),start=1):
    update()
    print(W) #打印当前的权值
    #print(i) #当前迭代次数
    output = np.sign(np.dot(X,W.T))
    print(output,Y)
    if(output == Y).all():
        print("Done,epoch=",i)
        break



#正样本
x1=[3,3]
y1=[4,3]

#负样本
x2=[1]
y2=[1]

x3=[2,3]
y3=[1,4]

#计算分界线的斜率和截距
k=-W[1]/W[2]
d=-W[0]/W[2]

print("output: ",np.sign(np.dot(X,W.T)))
xdata=np.linspace(0,5)
plt.figure()

plt.plot(xdata,xdata*k+d,"r") #r -red
plt.plot(x1,y1,"bo")
plt.plot(x2,y2,"yo")
# plt.plot(x3,y3,"g")
plt.show()


