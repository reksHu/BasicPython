import os
import sys
import datetime as dt
import numpy as np

def python_sum(n):
    a =[ i**2 for i in range(n)]
    b = [i**3 for i in range(n)]
    c =[]
    for i in range(n):
        c.append(a[i]+b[i])

def numpy_sun(n):
   return np.arange(n)**2 +np.arange(n)**3

start = dt.datetime.now()
print("Now:",start)
# python_sum(100000)
n = numpy_sun(100000)
print(n)
end =dt.datetime.now()
print("end:",end)
print("during:",(end-start).microseconds)
