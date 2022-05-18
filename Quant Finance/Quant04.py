import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf	
##### MPLFINANCE DOCUMENTATION #####
# https://pypi.org/project/mplfinance/
####################################
import matplotlib.dates	as mdates
import pandas as pd
#import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv("C:\\Users\\andre\\OneDrive\\Documents\\TradeBot\\Quant Finance\\tsla.csv", parse_dates = True, index_col = 0)

df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods = 0).mean()
#print(df.head())
#print(df.tail())

#mpf.plot(df,type='candle',mav=(3,6,9),volume=True,show_nontrading=True)

kwargs = dict(type='candle',mav=(150,50),volume=True,figratio=(10,8),figscale=0.75)


##### EDIT GRAPH STYLES #####
# https://github.com/matplotlib/mplfinance/blob/master/examples/customization_and_styles.ipynb
#############################

#mpf.plot(df,**kwargs,style='classic')
mpf.plot(df,**kwargs,style='yahoo')

