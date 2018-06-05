class Human(object):
    classObj ="this is class object"
    __hideObj = "this is hidden object"
    def __init__(self,name,age):
        self.__name = name
        self.__age=age
        print("object borned,id:%s" %str(id(self)))
    def __call__(self, *args, **kwargs):
        pass
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def getAge(self):
        return  self.__age

    def toString(self):
        # return "%name=(name),age=(age)" %{"name":self.__name,"age":str(self.__age)}
        return "name=%(name)s,age=%(age)d" %{"name":self.__name,"age":self.__age}
    def __del__(self):
        print("object del,id:%s" %str(id(self)))

h = Human('rex',30)
print(h.toString())

h2 = h.__class__('a',18)
print(h2.toString())
print(h2.__dict__)
print(h2.classObj)
h2.addre="chengdu"
print(h2.addre)
