import talib
import numpy as np
from binance.client import Client
from binance.enums import *
import pickle

apikey = 'NYccENDwcmYnVI9mMu3sGlS9BW6XO6IkDiFaN1OYPFJrmuL0PQWVEN0mJrcmo8JZ'
secretkey = 'oUXKjZvt89KNrPqO5XBRR0J1ioS3stnfBoI5YtUUXnCzaIquVNtb9Hgo4XnWmdJ2'

client = Client(apikey,secretkey)

# "1 day ago UTC"
# "1 Dec, 2017", "1 Jan, 2018"
# "1 Jan, 2017"
def store_klines_to_file(symbol,period):
    if period == '1m':
        candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
    elif period == '5m':
        candles = client.get_klines(symbol, Client.KLINE_INTERVAL_5MINUTE)
    elif period == '15m':
        candles = client.get_klines(symbol, Client.KLINE_INTERVAL_15MINUTE)
    elif period == '1H':
        candles = client.get_klines(symbol, Client.KLINE_INTERVAL_1HOUR)
    elif period == '4h':
        candles = client.get_klines(symbol, Client.KLINE_INTERVAL_4HOUR)
    return np.array(candles)

sample = store_klines_to_file('BNBUSDT','1m')
print(sample)