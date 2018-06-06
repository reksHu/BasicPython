import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md
import platform
# 布尔:?
# 有符号字节:b
# 无符号字节:B
# 整形:i  # 默认为i8 = int8, i2=int16, i4=int32
# 无符号整形: u / u2 / u4 / u8  # u=unicode 8,u2= unicode 16
# 浮点：f2 / f4 / f8 = float16 / float32 / float64
# 复数:c8 / c16
# 时间增量:m
# 时刻:M(具有年月日)
def dmy2ymd(dmy):
    #print("dmy:",dmy,type(dmy)) # dmy 为byte类型
    return dt.datetime.strptime(dmy.decode('utf-8'),'%d-%m-%Y').date().strftime("%Y-%m-%d")
    # return dt.datetime.strptime(str(dmy,'utf-8'),'%d-%b-%y').date().strftime("%Y-%m-%d")




def read_csv():
    fileName ='aapl2.csv'
    dates, openPrice, highPrice, lowPrice, closePrice,volumn = \
        np.loadtxt(fileName,delimiter=',',usecols=(1,3,4,5,6,7),  #usecols=(0,1,2,3,4,5),  usecols=(1,3,4,5,6,7)
                   unpack=True,dtype=np.dtype('M8[D],f8,f8,f8,f8,f8'),#M8[D]以日为单位，取八个字节
                   converters={1:dmy2ymd}) #converters={1:dmy2ymd}
    return dates, openPrice, highPrice, lowPrice, closePrice,volumn

def init_chat(first_day, last_day):
    f_daystr = first_day.astype(md.datetime.datetime).strftime('%d %b %y')
    l_daystr = last_day.astype(md.datetime.datetime).strftime('%d %b %y')
    #gcf = get current figure, 240/255将图的背景设置为 浅灰色, set_facecolor可以接收0-1之间的浮点数表示颜色
    mp.gcf().set_facecolor(np.ones(3) * 240/255)
    mp.title('Candlestick Chart',fontsize=14)
    mp.xlabel("Trading Days From %s to %s" %(f_daystr,l_daystr),fontsize=12 )
    mp.ylabel("Stock Price (USD) of Apple Inc.",fontsize=12)

    ax = mp.gca()  # get current axis
    ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO)) # MO = monday
    # ax.xaxis.set_major_locator(md.MonthLocator(bymonthday=md.MONTHLY)) #monthly
    ax.xaxis.set_minor_locator(md.DayLocator())#设置主定位器
    ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %y')) #设置格式化器

    #显示刻度
    mp.tick_params(which='both',top=True,right=True, labelright=True,labelsize=10) #水平轴和垂直轴都有
    mp.grid(linestyle=':')

def show_chat():
    mng = mp.get_current_fig_manager()
    # if(platform.system()=='Windows'):
    #     mng.window.state("zoomed") #在window系统里面设置窗口最大化
    # else:
    #     mng.resize(*mng.window.maxsize()) #在非windows系统中设置窗口的最大化
    mp.show()

def draw_chat(dates, openPrice, highPrice, lowPrice, closePrice,volumn):
    dates = dates.astype(md.datetime.datetime)
    up = closePrice-openPrice>=1e-2  #浮点数比较，超过0.01分, 1e-2 =0.01, 股票上涨，阳线
    down = openPrice-closePrice >=1e-2  #股票跌，阴线
    fc = np.zeros(dates.size,dtype='3f4') # 设置前景色
    ec = np.zeros(dates.size,'3f4') #设置边缘色
    fc[up] =(1,1,1)   #布尔过滤器,对上涨数据定义为白色
    fc[down]=(0,0.5,0)  #(0,0.5,0) 对应为红绿蓝
    ec[up],ec[down] =(1,0,0),(0,0.5,0)
    print(ec)
    mp.bar(dates, highPrice - lowPrice, 0, lowPrice,align='center', color=fc, edgecolor=ec)
    mp.bar(dates,closePrice-openPrice,0.8,openPrice,align='center',color=fc,edgecolor=ec)

dates, openPrice, highPrice, lowPrice, closePrice,volumn = read_csv()
#计算算数平均值
print(np.mean(openPrice))

init_chat(dates[0],dates[-1])
draw_chat(dates, openPrice, highPrice, lowPrice, closePrice,volumn)
show_chat()