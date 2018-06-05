# 股票波动率:
# std(T)/menu(T)/(sqrt(1/trading_days) ): 将波动率平均到每一天
# menu(T) :平均值

import numpy as np
def read_csv():
    fileName="aapl2.csv"
    close_prices = np.loadtxt(fileName,delimiter=',',usecols=(6),unpack=True, dtype="f8")
    return  close_prices

def calc_volatility(close_prices):
    log_prices = np.log(close_prices)
    log_diff = np.diff(log_prices)
    close_prices_std = np.std(log_diff)
    volatility = close_prices_std / log_diff.mean() / np.sqrt(1/252)  #波动率,一年有252个交易日，波动量比平均量，再平均到每一天
    return volatility  #年华波动收益率, 表示一年的收益为 129.274789911%

close_prices =  read_csv()

volatility = calc_volatility(close_prices)
print(volatility)