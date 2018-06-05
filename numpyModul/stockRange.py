# 练习:计算股票价格的波动范围：在一定时期内最高的最高价 - 最低的最低价
import  numpy as np
def read_csv():
    fileName="aapl2.csv"
    high_prices, low_prices =  np.loadtxt(fileName,delimiter=',',usecols=(4,5),unpack=True)
    return  high_prices,low_prices


high_prices,low_prices = read_csv()
stock_range = np.max(high_prices) - np.min(low_prices)
print(stock_range)