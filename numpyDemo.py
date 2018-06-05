import numpy as np

narray = np.random.rand(3,2)
print(narray)
for a in narray:
    print(a)
    for i in a:
        print(i)