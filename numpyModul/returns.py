import numpy as np

def read_csv():
    fileName = "aapl2.csv"
    high_prices, low_prices,close_prices  = np.loadtxt(fileName, delimiter=',', usecols=(4, 5,6), unpack=True)
    return high_prices, low_prices, close_prices

def auto_returns(close_prices):
    dif_prices = np.diff(close_prices)
    returns = dif_prices/close_prices[:-1]
    print(returns)
    std = np.std(returns)
    print(std)

def man_returns(close_prices):
    diff = np.zeros(close_prices.size-1)
    for index, close_price in enumerate(close_prices):
        if(index>0):
            diff[index-1]= close_price-close_prices[index-1]

    returns = diff/close_prices[:-1] #分析的 样本
    diff_min = returns - np.mean(returns) #离差
    diff_min_sqrt = diff_min**2 #离方差
    whole_diff_sqrt = np.mean(diff_min_sqrt) #总体方差
    whole_stad_sqrt = np.sqrt(whole_diff_sqrt) #总体标准差
    # whole_std = np.sqrt(  ((returns-returns.mean())**2).mean() )
    print(whole_stad_sqrt)

#对数收益率
def auto_log_returns(close_prices):
    log_returns = np.log(close_prices)
    diff_returns = np.diff(log_returns)
    std = np.std(diff_returns)
    print(std)

def random_std():
    s = np.random.rand(500)
    print(s)
    diff = np.diff(s)
    returns = diff/s[:-1]
    std = np.std(returns)
    print(std)

high_prices, low_prices, close_prices = read_csv()
auto_returns(close_prices)
# # print(np.mean(close_prices))
# # man_returns(close_prices)
# auto_log_returns(close_prices)

random_std()