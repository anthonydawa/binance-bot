
from market_process import market_process
from market import finalized, get_cached_market
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

import time
import threading


from binance.client import Client
from binance.enums import *



apikey = 'NYccENDwcmYnVI9mMu3sGlS9BW6XO6IkDiFaN1OYPFJrmuL0PQWVEN0mJrcmo8JZ'
secretkey = 'oUXKjZvt89KNrPqO5XBRR0J1ioS3stnfBoI5YtUUXnCzaIquVNtb9Hgo4XnWmdJ2'

client = Client(apikey,secretkey)

def to_caps(arr):
    y = []
    for x in arr:
        y.append(x.upper()) 
    return y  

markets = get_cached_market()
market_caps = to_caps(markets)
channels = ['kline_5m','kline_15m','kline_1h','kline_4h','trade']

kline = []

for m in markets:
    kline.append([])

for index,m in enumerate(markets):
    t = threading.Thread(target=market_process, args=(markets[index],kline[index],))
    t.start()
    time.sleep(1)


def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            try:
                for index,m in enumerate(market_caps):
                    if oldest_stream_data_from_stream_buffer['data']['k']['x'] == True:
                        if m == oldest_stream_data_from_stream_buffer['data']['k']['s']:
                            kline[index].append(oldest_stream_data_from_stream_buffer)
            except Exception:
                # not able to process the data? write it back to the stream_buffer
                binance_websocket_api_manager.add_to_stream_buffer(oldest_stream_data_from_stream_buffer)



if __name__ == '__main__':
    binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com", output_default='dict')
    worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
    worker_thread.start()
    kline_stream_id = binance_websocket_api_manager.create_stream(channels, markets)

    while True: 
        try:
            pass
        except KeyboardInterrupt:
            print("\nStopping ... just wait a few seconds!")
