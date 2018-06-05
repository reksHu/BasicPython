def myfun(a,b,c):
    print("a-->",a)
    print("b-->", b)
    print("c-->", c)

#位置参数
myfun(1,2,3)

#序列参数,*s 以元组的方式传递给函数，函数按照顺序解析
s = [11,22,33]
myfun(*s)


s2 =(1.1,2.2,3.3)
myfun(*s2)

s3="abc"
myfun(*s3)

print("#"*20, 'key word parameters', "#"*20)
myfun(a='a1', b='a2',c='a3')
print("*"*20)
myfun(c='a1', a='a2', b='   a3')
print("*"*20)
d = {'a': 10, 'b': 20, 'c': 30}
myfun(**d)


print("#"*20, 'composite parameters', "#"*20)
myfun(100, *(200, 300))
print("*"*20)
myfun(100, **{'b': 200, 'c': 300})
print("*"*20)
myfun(*[110], 220, *(330,))

