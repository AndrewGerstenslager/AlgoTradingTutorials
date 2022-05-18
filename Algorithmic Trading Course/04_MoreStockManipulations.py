import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from matplotlib.finance import candlestick_ohlc
import mpl_finance as mpf
from matplotlib.dates as mdates
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', None)
style.use('ggplot')



df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods = 0).mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volumne'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan = 1, sharex= ax1)
ax1.xaxis_date()

plt.show()


