from numpy import mat,matrix,shape,multiply
ss= mat([1,2,3])
print(ss)

sm = matrix([1,2,3])
print(sm)
print("************")
jj=mat([[1,2,3],[3,5,9]])
print(jj,shape(jj))
print(jj[0,:])

mul = multiply(jj[0,:],jj[1,:])


m1=matrix([[1,0],[4,1],[3,2]])
print(m1)
print(shape(m1.T))