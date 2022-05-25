
from f7 import AverageTrueRange, idx_array, initial_klines, upper_case, ExpMa, watch_closed, watch_data, watch_loss
from helper_func import upper_case
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

import time
import threading

from binance.client import Client
from binance.enums import *



apikey = 'NYccENDwcmYnVI9mMu3sGlS9BW6XO6IkDiFaN1OYPFJrmuL0PQWVEN0mJrcmo8JZ'
secretkey = 'oUXKjZvt89KNrPqO5XBRR0J1ioS3stnfBoI5YtUUXnCzaIquVNtb9Hgo4XnWmdJ2'

client = Client(apikey,secretkey)

markets = ['uniusdt']
market_caps = upper_case(markets)
channels = ['kline_1m']

mrkt = 'UNIUSDT'
symbol = 'UNI'
dec = 4

latest_klines = initial_klines(market_caps)
latest_closed = idx_array(latest_klines,4)
latest_200ma = ExpMa(latest_closed,200)
latest_50ma = ExpMa(latest_closed[-55:],50)
latest_atr = AverageTrueRange(latest_klines)

ma200 = []
ma50 = []
atr15 = []

rsi14 = []
bullish = []

buffer_candle_unclosed = []
buffer_candle_closed = []

ctr = []
retries = []

stoploss = []
order = []


def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            try:
                is_it_closed = oldest_stream_data_from_stream_buffer['data']['k']['x']
                if is_it_closed == False:
                    # print(oldest_stream_data_from_stream_buffer['data']['k']['c'],'unclosed')
                    buffer_candle_unclosed.append(oldest_stream_data_from_stream_buffer)
                elif is_it_closed == True:
                    # print(oldest_stream_data_from_stream_buffer['data']['k']['c'],'closed')
                    buffer_candle_closed.append(oldest_stream_data_from_stream_buffer)
                    
            except Exception:
                # not able to process the data? write it back to the stream_buffer
                binance_websocket_api_manager.add_to_stream_buffer(oldest_stream_data_from_stream_buffer)
            



 



if __name__ == '__main__':
    binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com", output_default='dict')
    worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
    worker_thread.start()
    kline_stream_id = binance_websocket_api_manager.create_stream(channels, markets)
    try:
        while True:
            watch_data(buffer_candle_closed,latest_klines,latest_closed,ma200,ma50,atr15,rsi14,bullish)
            watch_loss(stoploss,symbol,mrkt,dec,buffer_candle_unclosed,order)
            watch_closed(ma200,ma50,atr15,rsi14,buffer_candle_closed,ctr,retries,stoploss,bullish,mrkt,symbol,dec,order)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping ... just wait a few seconds!")
        

