#函数重载

class functionClass:
    def __init__(self,num):
        self.num=num

    def __str__(self):
        return 'str overite'

    def __repr__(self):
        return "repr overite"
    def __add__(self, other):
        if(type(other)==functionClass):
            return self.num+other.num
        return self.num + other

f = functionClass(5)
f2 = functionClass(10)
# s = str(f)
print(f)
print(f+f2)
print(f+10)
