#练习2：编写一个数值，计算并打印其中每一个数字出现的个数，
# 如： 输入2234523
# 打印: 2 出现3次，3 出现1次....

text = input("input a word\n")
myset = set(text)
for x in myset:
    print('%s count: %d' %(x,text.count(x)))