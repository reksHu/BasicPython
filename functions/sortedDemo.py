# 将原来可迭代对象的数据进行排序，生成排序后的列表
# sorted(iteratble, key=None,reverse=False)
# key用来提供一个值，这个值作为排序的依据,可以是一个函数的引用

def mysort(arg):
    # print(arg)
    return abs(arg)

l=[5,-2,-4,0,3,1]
l2 = sorted(l,key=mysort)
# print(l2)

def sortname(arg):
    # print(arg[-1:-3:-1])
    return arg[-1:-3:-1]


name=['Tom','Jerry','Spike','Tyke']
l2 = sorted(name,key=sortname)

#传入字典,使用sorted
names=[{'id':3,'name':'Tom'},{'id':2,'name':'Jerry'},{'id':5,'name':'Spike'},{'id':1,'name':'Tyke'}]
def mydic(d):
    print(d['id'])
    # return d.id
    return d['id']

l2 = sorted(names,key=mydic)
print(l2)