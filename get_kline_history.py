from hmac import new
from typing import cast
from binance.client import Client

from binance.enums import *

import pickle

import numpy as np

client = Client('vgDhGQw1VAJoB9lICjNc0sZNRIdruOBoDTIEOv6RXA265NisxvP8kEctcKu1c1Cb', '5xwAu0jnNVDiLnNsrhjAaRD6BmlRa2O9nNm3g5GlT0ByIJv74zBu4Q8RWKzOps10')

def klines_init(symbol,days=1):
    for c in symbol:
        klines = client.get_historical_klines(c, Client.KLINE_INTERVAL_5MINUTE, f"{days} days ago UTC")
        file_name = c
        with open(file_name, 'wb') as file:
            pickle.dump(klines,file)

def get_200_latest_klines(dataset):
    array_data = []
    for p in dataset:
        with open(p,'rb') as dataset_file:
            new_data = pickle.load(dataset_file)  
            array_data.append(new_data[-201:])
    return array_data

def get_200_closed(dataset):
    closed_arr = []
    for data in dataset:
        arr = []
        for d in data:
            arr.append(d[4])
        closed_arr.append(arr)
    return closed_arr

def initial_klines(symbols,days=1):
    x = []
    for symbol in symbols:
        klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, f"{days} day ago UTC")
        last_200 = klines[-201:]
        x.append(last_200) 
    return np.array(x)




# klines = client.get_historical_klines('ADAUSDT', Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
# print(klines[0])
# print(klines[len(klines)-1])

# print(klines[0])
# klines_init(['ADAUSDT'])

# print(get_200_latest_klines(['ETHUSDT']))

# klines_init(['BTCUSDT','BNBUSDT'])