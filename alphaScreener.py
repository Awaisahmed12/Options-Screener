
import tweepy
APItoken = ""
auth = tweepy.OAuthHandler(APItoken, APItoken)
auth.set_access_token(APItoken,APItoken)
api = tweepy.API(auth)

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = "AlphaVantageApi Token"
tickers = ['AAL', 'AAPL', 'AMZN', 
'ACB', 'AMC', 'AMD', 'APHA', 
'BA', 'BABA', 'BAC', 'BP', 
'CGC', 'CRON', 'DAL', 'GILD', 
'GOOGL', 'GM', 'HAL', 'IDEX', 
'INO', 'INTC', 'JBLU', 'JPM', 
'KO', 'INTC', 'JNJ', 'KODK', 
'LYFT', 'MGM', 'MRO', 'MSFT', 
'NIO', 'NKE', 'NKLA', 'NOK', 
'NRZ', 'PFE', 'NVDA', 'PTON', 
'ROKU', 'SBUX', 'SIRI', 'SNAP', 
'SPY', 'SQ', 'T', 'TLRY', 'UAL', 
'UBER', 'USO', 'V', 'VOO', 'WKHS', 
'WMT', 'WORK', 'XOM', 'ZM', 'ZNGA']

#free version of the API only allows five uses per hour
#tickers = ['AAPL', 'AMZN', 'TSLA', 'NVDA', 'WMT']
#thisDict = { "Ticker" : 0.00}


for stock in tickers:
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=stock, interval = '60min', outputsize = 'full')
    #print(data)
    #thisDict[stock] = data
    #i = 1
    #while i==1:
    #    data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
    #    data.to_excel("output.xlsx")
    #    time.sleep(60)

    close_data = data['4. close']
    percentage_change = close_data.pct_change()
    #print(percentage_change)
    last_change = percentage_change[-1]
    if abs(last_change) > 0.004:
        api.update_status(status = ("TICKER: " + stock + "\n" + "PERCENT CHANGE: " + str(last_change) ))
    time.sleep(20)