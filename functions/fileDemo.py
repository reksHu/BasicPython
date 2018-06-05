#coding: UTF-8 -*-

def openfile():

    f = open("zipDemo.py",mode='r',encoding="UTF-8")
    # for l in f.readlines():
    #     print("###",l.rstrip('\n'),"###")

    print(f.name)
    print(f.fileno())
    f.close()

# openfile()

def fileWrite():
    f = open('test.txt',mode='a',encoding="UTF-8")
    for x in range(4):
        s='my write'+str(x)+"\n"
        f.writelines(s)
    f.close()

fileWrite()