import numpy as np
an = np.arange(10,30,2)
print(an, type(an),an.dtype,an.shape,an.ndim)
print([x for x in range(10,30,2)])

two_dim = np.array([ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ], float)
print(two_dim.dtype,two_dim.shape,two_dim.ndim)

three_dim = np.array([
    [
        np.arange(1,5),
        np.arange(3,7),
        np.arange(10,14)
    ],
    [
        np.arange(5,9),
        np.arange(20,24),
        np.arange(28,32)
    ]
], dtype=float)

print(three_dim,three_dim.ndim,three_dim.shape)
print("dim 0:",three_dim[0][1][1],three_dim[0,1,1])
t = np.dtype(np.int16)
three_dim = np.arange(1,25).reshape(2,3,4).astype(t)
print(three_dim.shape,type(three_dim),three_dim.dtype)

print("{:4}".format(three_dim[0,1,1]))