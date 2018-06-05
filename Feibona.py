#打印前十个斐波那契数
def febis1():
    myarr = [1, 1]
    feibona = []
    n = 2
    while n < 11:
        nextItem = myarr[n - 1] + myarr[n - 2]
        myarr.insert(n, nextItem)
        n += 1

    for x in myarr:
        print("%-5d" % x, end='')

#方法二:
def febis2(maxLen):
    febi=[0,1]
    for x in range(maxLen+1):
        febi.append(febi[-2]+febi[-1])

    for x in febi:
        print("%5d" %x,end=' ')


febis2(60)