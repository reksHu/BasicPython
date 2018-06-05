#大端练习

import numpy as np

a1 =  np.array([ (2,3),(4,5)])

# print(a1, a1.ndim, a1.shape)

a2 = np.array([ [2,3],[4,5] ])

# print(a2,a2.ndim,a2.shape)

a3= np.array([
    [ [[1,2,3,4],[5,6,7,8],[9,10,11,12]] ,
    [ [13,14,15,16],[17,18,19,20],[21,22,23,24] ] ]
])
# print(a3, a3.ndim,a3.shape)

a4= np.array([
    ( ((1,2,3,4),(5,6,7,8),(9,10,11,12)) ,
       ((13,14,15,16),(17,18,19,20),(21,22,23,24) ) )
    ,( ( (25,26,27,28),(29,30,31,32),(33,34,35,36) ),
      ( (37,38,39,40), (41,42,43,44),(45,46,47,48) ))
],dtype="<(2,3,4)i4")

# print(a4, a4.ndim,a4.shape,a4.dtype)

n_str = np.array([ ['hello world'],['hello python'] ],dtype=(np.str_,14))
print(n_str,n_str.dtype,n_str.ndim)

b = np.array( [(1,2,3,4,5),(6,7,8,9,10),(1,1,1,1,1)] ,dtype=(int,5)) #规定每一个元素是int类型，并且每个元素由5个元素构成
b = np.array( [ [1,2,3,4,5],[6,7,8,9,10] ] ,dtype=(int,5)) #这种定义是错误的
print(b)

b2= np.array([ ( (1,2,3),(3,4,5) ),((7,8,11),(9,10,12)) ] ,dtype=((np.uint8,3),2))
print(b2,b2.ndim,b2.shape)
