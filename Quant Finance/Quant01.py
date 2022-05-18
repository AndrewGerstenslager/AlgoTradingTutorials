import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
#import pandas_datareader.data as web

style.use('ggplot')

#2000, January, 1st

'''
start = dt.datetime(2000,1,1)

#2016, December, 31st
end = dt.datetime(2016,12,31)

df = web.DataReader('TSLA', 'yahoo', start, end)
#print(df.head())
df.to_csv('tsla.csv')
'''


df = pd.read_csv("C:\\Users\\andre\\OneDrive\\Documents\\TradeBot\\Quant Finance\\tsla.csv", parse_dates = True, index_col = 0)

df['Adj Close'].plot()
plt.show()

