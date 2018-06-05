import numpy as np
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    #print("dmy:",dmy,type(dmy)) # dmy 为byte类型
    cDays = (dt.datetime.strptime(dmy.decode('utf-8'),'%d-%m-%Y').date()-dt.date.min).days
    return  cDays


def get_open_price():
    fileName = 'aapl2.csv'
    times, open_price,close_prices ,volumns, = np.loadtxt(fileName, delimiter=',',usecols=(1,3,6,7),
                                                   unpack=True,  converters={1:dmy2ymd})
    return times, open_price,close_prices, volumns

def auto_VWAP(close_prices,volumns):
    vwap = np.average(close_prices,weights=volumns)
    return vwap

def man_VWAP(close_prices,volumns):
    tvw,vwa =0.,0.
    for close_price, volumn in zip(close_prices,volumns):
        tvw +=close_price*volumn
    vwa = tvw/np.sum(volumns)
    print(vwa)

def auto_TWAP(times,close_prices):
    twap = np.average(close_prices,weights=times)
    print(twap)

times,price,close_prices,volumns = get_open_price()
print(np.mean())
# print(close_prices)
# print( volumns)
# man_VWAP(close_prices,volumns)
print(auto_VWAP(close_prices,volumns))
# print(times)
auto_TWAP(times,close_prices)
