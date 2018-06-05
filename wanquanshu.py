#完全数:
# 完全数指除自身以外的所有的因数相加之和等于自身的数
# 1 + 2 + 3 = 6
# 求4 - 5 个完全数并打印

maxNum = 3
while(maxNum<10000):
    l = [x for x in range(1,maxNum) if maxNum%x==0 and maxNum//x>0]
    if(sum(l) == maxNum):
        print(l)
        print(maxNum)
    maxNum+=1
