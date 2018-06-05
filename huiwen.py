#输入任意一个字符串，判断是否为回文， 12321则是回文

while True:
    text = input('please input a sentence\n')
    listT= list(text)
    reversedT = reversed(text)
    reversedListT = list(reversedT)
    if(listT == reversedListT):
        print("It's huiWen")
    else:
        print("it's not huiWen")


#方法二
#  reversedT = text[::-1]
# if(reversedT == list(text)): print('huiwen')