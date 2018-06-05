# 中位数:将多个样本按大小顺序排列，居于中间位置的元素就是中位数。
# 可以反应出相对公平的数值。
import  numpy as np

def read_csv():
    fileName = "aapl2.csv"
    open_prices = np.loadtxt(fileName,delimiter=',',usecols=(3),unpack=True)
    return  open_prices

def auto_median(open_prices):
    median = np.median(open_prices)
    print(median)

def man_median(open_prices):
    op = np.sort(open_prices)
    print(open_prices[int((op.size-1)/2)],open_prices[int(op.size/2)])
    print(op)
    a1 = int((op.size-1)/2)
    a2 = int(op.size/2)
    print(a1,a2,op[a1],op[a2])
    median = (op[a1] + op[a2])/2
    print(median)
open_prices = read_csv()
auto_median(open_prices)
man_median(open_prices)
