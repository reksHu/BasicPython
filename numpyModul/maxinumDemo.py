import numpy as np

a = np.random.randint(10,100,27).reshape(3,3,3)
b = np.random.randint(10,100,27).reshape(3,3,3)
print(a)
print(np.max(a),np.min(a))
print(np.maximum(a,b))