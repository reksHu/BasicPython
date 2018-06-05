class A:
    className="class A"
    @staticmethod
    def Add(a,b):
        return  a+b
    a,b = 2,6
    @classmethod
    def Add2(cls):
        return cls.Add(cls.a,cls.b)
    @property
    def cName(self):
        return self.className
    @cName.setter
    def cName(self,n):
        self.className=n


a = A()
print(a.cName)
a.cName="changed"
print(a.cName)

# result = A.Add(3,5)
# print(result)
# a=A()
# print(a.Add(3,5))
#
# print(A.Add2())
