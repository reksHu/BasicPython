class A:
    def __call__(self, *args, **kwargs):
        print("args:",args,"kwargs:",kwargs)
        for ar in args:
            print(ar)

        for k,v in kwargs.items():
            print(k,v)



# a = A()
# a(*(100,),**{"a":300,"b":301})
# # a((100,200))

class MySum:
    totalCount=0
    def __call__(self, *args):
        self.totalCount = sum(args)
        return  self.totalCount


# s = MySum()
# result = s(200,300,500)
# print(result)

class Odd:
    def __init__(self,start,end):
        self.start=start
        self.end =end
        self.current =start
    def __next__(self):
        print("call next")
        if(self.current>self.end):
            raise StopIteration("stop iteration")
        if(self.current %2==0):
            self.current+=1
        r = self.current
        self.current=r+2
        # self.start=self.current
        return r
    def __iter__(self):
        print("iteration function calling")
        self.current =self.start
        return self
o =Odd(2,10)
print(next(o))
for x in o:
    print(x)
print([x for x in o])
