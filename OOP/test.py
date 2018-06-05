# from Human import *
# from human import Human
from .human import Human
h1 = Human('aa',18)
print(h1.getName())
# h=None
h2=h1

# from garbageDemo import c1
# from garbageDemo import myClass
from .garbageDemo import myClass

c = myClass()
c.cPrint()



