# 用filter函数将1-100之间所有的素数prime放入列表中
# 在一般领域，对正整数n，如果用2到 n 开根 之间的所有整数去除，均无法整除，则n为质数。
# 质数大于等于2 不能被它本身和1以外的数整除
import math
def myprime(n):
    for x in range(2,int(math.sqrt(n))+1):
        if n%x==0: #不是素数
            return False
        return True

result = filter(myprime,range(1,101))
print(list(result))