class Person:
    def __init__(self,name,age):
        self.__name=name
        self.age=age

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self,name):
        self.__name=name

    def study(self,lessonName):
        print("Person named %(name)s is studing %(lesson)s" %{"name":self.Name,"lesson":lessonName})


class Student(Person):
    def __init__(self,name,age):
        super(Student,self).__init__(name,age)

    def study(self,lesionName):
        print(self.Name," is studying ",lesionName,"age:",self.age)
        # self.__class__.__base__.study(self,lesionName)
        # Person.study(self,lesionName)
        # s = super()
        # s.study(lesionName)
        # super(Student,self).study(lesionName)


p = Person("Rex",18)
# p.study("AI")
# print(p.Name)
s = Student("Rex",30)
s.Name="HongChun"
s.study('python')
# super(Student,s).study("AI")
# Student.study(s,"AI")
# print(Student.__base__,s.__class__.__base__)