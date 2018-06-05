#打印1-20之间的整数，每隔5个数换行
#1 2 3 4 5
#6 7 8 9 10

for x in range(1,21):
    # print(x,sep=',', end=' ')
    print(str(x).center(10),end='')
    if(x%5==0):
        print()