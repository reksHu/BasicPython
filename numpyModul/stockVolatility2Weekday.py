#求每一周中每天的波动情况

import  datetime as dt
import  numpy as np

def read_csv():
    fileName ="aapl2.csv"
    dates , close_prices = np.loadtxt(fileName,delimiter=',',
                                      usecols=(1,6),unpack=True,dtype=np.dtype('i8,f8'), converters={1:convert_weeks})
    return  dates, close_prices



def convert_weeks(dmy):
    str_date = str(dmy,encoding='utf-8')
    d = dt.datetime.strptime(str_date,'%d-%m-%Y')
    # d = dt.datetime.strptime(dmy.decode('utf-8'),'%d-%m-%Y')
    return d.weekday()

def calc_average_prices(weeks,close_prices):
    average_week_prices=np.zeros(5)
    for weekday in range(average_week_prices.size):
        average_week_prices[weekday] = np.take(close_prices, np.where(weekday == weeks)).mean()

    print(np.where(weeks==0))
    print(np.where(weeks ==4))
    return  average_week_prices


weeksday = ("MON", "TUE", "WED", "THU", "FRI", "SAY", "SUN")
weeks, close_prices = read_csv()
print(weeks)
average_week_prices = calc_average_prices(weeks,close_prices)
print(average_week_prices.size)
max_index = np.argmax(average_week_prices)
min_index = np.argmin(average_week_prices)
for index, value in enumerate(average_week_prices):
    week_prices = weeksday[index]
    print(weeksday[index] , ": " ,value,"(max)" if(index==max_index) else '(min)' if(index==min_index) else '')