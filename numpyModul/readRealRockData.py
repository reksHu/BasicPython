import requests
import json
import csv

def get_stock_info():
    url="https://gupiao.baidu.com/api/stocks/stockweekbar?from=pc&os_ver=1&cuid=xxx&vv=100&format=json&stock_code=sh000001&step=3&start=&count=160&fq_type=no&timestamp=1525589069180"
    data = requests.get(url)
    data_str = str(data.content,encoding='utf-8')
    # json_str = json.dumps(data_str)
    # print(json_str)
    json_obj = json.loads(data_str)
    mashData = json_obj["mashData"]
    for index, obj in enumerate(mashData):
        date = obj["date"]
        kline =obj["kline"]
        print(date,kline,kline["open"])
    return  mashData


def write_csv(mashData):
    fileName = "stock.csv"
    with open(fileName,"w",newline="") as file:
        fieldNames=["stockId",'date',"open",'high','low','close','volume']
        writer = csv.DictWriter(file,fieldnames=fieldNames)
        writer.writeheader()
        for index, obj in enumerate(mashData):
            date = obj["date"]
            klines = obj["kline"]
            row = {"stockId":"sh000001","date":date,"open":klines['open'],"high":klines["high"],
                   "low":klines["low"],"close":klines["close"],"volume":klines["volume"]}
            writer.writerow(row)

import  numpy as np
import datetime as dt
def read_stock_csv():
    fileName = "stock.csv"
    dates, open_prices,high_prices,low_prices,close_prices = \
        np.loadtxt(fileName,delimiter=',',converters={0:convert_date},dtype="M8[D],f8,f8,f8,f8",
                   skiprows=1,unpack=True,usecols=(1,2,3,4,5))
    return dates, open_prices,high_prices,low_prices,close_prices

def convert_date(csv_date):
    # d_str = csv_date.decode('utf-8')
    d_str = str(csv_date,encoding='utf-8')
    d =dt.datetime.strptime(d_str,'%Y%m%d')
    return d.date().strftime("%Y-%m-%d")

def convert_weeks(csv_date):
    # np.loadtxt(fileName, delimiter=',', converters={0: convert_weeks}, dtype="i8,f8,f8,f8,f8",
    #            skiprows=1, unpack=True, usecols=(0, 1, 2, 3, 4))
    d_str = str(csv_date, encoding='utf-8')
    d = dt.datetime.strptime(d_str, '%Y%m%d')
    print(d.weekday())
    return d.weekday()

def stock_volatility(close_prices):
    log_prices= np.log(close_prices)
    diff_prices = np.diff(log_prices)
    prices_std = np.std(diff_prices)
    volatility = prices_std/diff_prices.mean()/np.sqrt(1/252)
    print(volatility)

mashData = get_stock_info()
write_csv(mashData)
# dates, open_prices,high_prices,low_prices,close_prices= read_stock_csv()
# stock_volatility(close_prices)
# print(dates)

# a= np.array( [['20150504'],['20180506']],dtype='M8[]')
# print(a)
def test_datetime_nat_casting(self):
    a = np.array('NaT', dtype='M8[D]')
    b = np.datetime64('NaT', '[D]')
    # Arrays
    print(a.astype('M8[s]'), np.array('NaT', dtype='M8[s]'))
    print(a.astype('M8[ms]'), np.array('NaT', dtype='M8[ms]'))
    print(a.astype('M8[M]'), np.array('NaT', dtype='M8[M]'))
    print(a.astype('M8[Y]'), np.array('NaT', dtype='M8[Y]'))
    print(a.astype('M8[W]'), np.array('NaT', dtype='M8[W]'))