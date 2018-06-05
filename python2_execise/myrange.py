#生成一个自定义与range函数一样功能的 新函数myrange

def myrange(start,stop=None,step=None):
    if(stop==None):
        stop=start
        start = 0
    if(step==None):
        step=1

    while start<stop:
        yield start
        start = start+step

def myrange2(s,*args):
    return range(s,*args)


print([x for x in myrange(11,20,2)])