import numpy as np

l = np.arange(1,9).reshape(2,4)
r = np.arange(10,12).reshape(2,1)

print(l)
print(r)

h = np.hstack((l,r))
print(h)


v_row = np.column_stack((l,r))
print(v_row)

a = np.arange(20,35).reshape(3,5)
b = np.row_stack((h,a))
print("*******")
print(b)
print("*******")

print(np.vsplit(b,5))

c = np.arange(1,17).reshape(4,4)
print(np.vsplit(c,np.array([3,5])))

print("******深度组合*****")
d = np.arange(1,7).reshape(2,3)
e= np.arange(11,17).reshape(2,3)
f = np.dstack((d,e))
print(f)

print(f[0].transpose())

