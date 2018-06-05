#线性神经网络 -- 异域问题 true/false
#异域 0^0 =0 ; 0^1=1; 1^0 = 1; 1^1 =0
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1,0,0,0,0,0],
    [1,0,1,0,0,1],
    [1,1,0,1,0,0],
    [1,1,1,1,1,1]
])

Y = np.array([-1,1,1,-1])

W = (np.random.random(6)-0.5)*2

rl = 0.11
output=0
def update():
    global rl,X,Y,output,W
    output = np.dot(X,W.T)
    W_change =(rl * (Y-output.T).dot(X))/X.shape[0]
    W = W+W_change

def calcuate(root,x):
    a = W[5]
    b = W[2]+x*W[4]
    c = x*x*W[3] + x*W[1]+W[0]
    if(root==1):
        return -b+ np.sqrt(b*b-4*a*c)
    elif(root==2):
        return b+np.sqrt(b*b-4*a*c)

n=0
for i,x in enumerate(range(1000),start=1):
    n=i
    update()
print("Done,epoch=",n)
#正样本
x1=[0,1]
y1=[1,0]

#负样本
x2=[0,0]
y2=[1,1]

O = np.dot(X,W.T)
print(O)

xdata = np.linspace(-2,5)
plt.figure()

plt.plot(xdata,calcuate(1,xdata),"r")
plt.plot(xdata,calcuate(2,xdata),"r")

plt.plot(x1,y1,"yo")
plt.plot(x2,y2,"bo")
plt.show()

