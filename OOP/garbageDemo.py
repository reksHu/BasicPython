class garbage(object):
    def __init__(self,name):
        self.__name=name
        print("%(name)s borned,id=%(id)s" %{"name":name,"id":str(id(self))})
    def __del__(self):
        print("%(name)s deleted, id=%(id)s" %{"name":self.__name,"id":str(id(self))})



class myClass(object):
    name="my class"
    def __init__(self):
        pass
    def cPrint(self):
        print('hello')
