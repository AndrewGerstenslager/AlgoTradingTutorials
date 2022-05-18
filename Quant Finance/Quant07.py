import bs4 as bs
import datetime as dt
import os
from pandas_datareader import data as pdr
import pickle
import requests
import fix_yahoo_finance as yf
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf	
##### MPLFINANCE DOCUMENTATION #####
# https://pypi.org/project/mplfinance/
####################################
import matplotlib.dates	as mdates
import pandas as pd
import pandas_datareader.data as web

#yf.pdr_override

def save_sp500_tickers():
	resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	soup = bs.BeautifulSoup(resp.text, 'lxml')
	table = soup.find('table', {'class': 'wikitable sortable'})
	tickers = []
	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[0].text
		ticker = ticker[:-1]
		tickers.append(ticker)

	with open('sp500tickers.pickle','wb') as f:
		pickle.dump(tickers, f)

	#print(tickers)

	return tickers


def save_sp500_tickers2():
	resp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
	soup = bs.BeautifulSoup(resp.text, "lxml")
	table = soup.find("table",{"class":"wikitable sortable"})
	tickers = []
	for row in table.findAll("tr")[1:]:
		ticker = row.findAll("td")[0].text
		mapping = str.maketrans(".","-")
		ticker = ticker.translate(mapping)
		tickers.append(ticker)
	with open("sp500tickers.pickle","wb") as f:
		pickle.dump(tickers,f)
		print(tickers)
	return tickers



def getYahooData(reload_sp500=False):
	if(reload_sp500):
		tickers = save_sp500_tickers()	
	else:
		with open('sp500tickers.pickle','rb') as f:
			tickers = pickle.load(f)

	if not os.path.exists('stock_dfs'):
		os.makedirs('stock_dfs')	

	start = dt.datetime(2000,1,1)
	end = dt.datetime(2016,12,31)

	for ticker in tickers:
		print(ticker)
		if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
			df = pdr.get_data_yahoo(ticker, start, end)
			df.reset_index(inplace=True)
			df.set_index("Date", inplace=True)
			df.to_csv('stock_dfs/{}.csv'.format(ticker))
		else:
			print('Already have {}'.format(ticker))

save_sp500_tickers2()
getYahooData()

def compile_data2():
	for count, ticker in enumerate(tickers):
		try:
			df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
			df.set_index('Date', inplace=True)

			df.rename(columns = {'Adj Close': ticker}, inplace=True)
			df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)

			if main_df.empty:
				main_df = df
			else:
				main_df.join(df, how='outer')

		except:
			print('stock_dfs/{}.csv'.format(ticker) + ' not found')

		if count % 10 == 0:
			print(count)


def compile_data():
	with open('sp500tickers.pickle','rb') as f:
			tickers = pickle.load(f)

	main_df = pd.DataFrame()

	for count, ticker in enumerate(tickers):
		#print(ticker)
		df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
		df.set_index('Date', inplace=True)

		df.rename(columns = {'Adj Close': ticker}, inplace = True)
		df.drop(['Open','High','Low','Close','Volume'],1, inplace=True)

		if main_df.empty:
			main_df = df

		else:
			main_df = main_df.join(df, how='outer')

		if count % 5 == 0:
			print(count)

	print(main_df.head())
	main_df.to_csv('sp500_joined_closes.csv')

compile_data2()
