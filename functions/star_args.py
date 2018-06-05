def myfun(*params):
    print(type(params),len(params))
    i=0
    # l = [index+p for index in range(i,len(params)) for p in params]
    for index in range(i,len(params)):
        print("the ",index+1, " parameter:",params[index], " Type:", type(params[index]))
        if(type(params[index]) is tuple):
            for x in params[index]:
                print(x)
    # index, p for index in range(1,len(params)) for p in params:
    #     print(p)

myfun(1,2,) # myfun(1,2)

myfun("100",200,"abc",300)
myfun((1.1,2.2,))