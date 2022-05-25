import unicorn_binance_websocket_api
import math
import requests
import sys
import time
import threading
import parse_data_from_stream as pdfs
import action_to_data as atd
import pickle

try:
    from binance.client import Client
except ImportError:
    print("Please install `python-binance`! https://pypi.org/project/python-binance/#description")
    sys.exit(1)

binance_api_key = ""
binance_api_secret = ""
channels = {'trade','kline_1m','kline_15m','depth20'}
chan = {'aggTrade', 'trade', 'kline_1m', 'kline_5m', 'kline_15m', 'kline_30m', 'kline_1h', 'kline_2h', 'kline_4h',
            'kline_6h', 'kline_8h', 'kline_12h', 'kline_1d', 'kline_3d', 'kline_1w', 'kline_1M', 'miniTicker',
            'ticker', 'bookTicker', 'depth5', 'depth10', 'depth20', 'depth', 'depth@100ms'}            
# arr_channels = {'!miniTicker', '!ticker', '!bookTicker'}
alt_markets = {'grtbtc','dotbtc','xrpbtc', 'adabtc','vetbtc', 'linkbtc','ltcbtc'}

def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is not False:
            x = pdfs.parse_data_from_stream(oldest_stream_data_from_stream_buffer)
            with open('streamed_data.pickle', 'ab') as f:
                if x:
                    pickle.dump(x,f)
                else:
                    pass
        else:
            time.sleep(0.01)

try:
    binance_rest_client = Client(binance_api_key, binance_api_secret)
except requests.exceptions.ConnectionError:
    print("No internet connection?")
    sys.exit(1)

binance_websocket_api_manager = unicorn_binance_websocket_api.BinanceWebSocketApiManager()

# start a worker process to move the received stream_data from the stream_buffer to a print function
worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
worker_thread.start()

# markets = []
# data = binance_rest_client.get_all_tickers()  
# for item in data:
#     markets.append(item['symbol'])

# private_stream_id_alice = binance_websocket_api_manager.create_stream(["!userData"],
#                                                                       ["arr"],
#                                                                       api_key=binance_api_key,
#                                                                       api_secret=binance_api_secret,
#                                                                       stream_label="userData Alice")

# private_stream_id_bob = binance_websocket_api_manager.create_stream(["!userData"],
#                                                                     ["arr"],
#                                                                     api_key="aaa",
#                                                                     api_secret="bbb",
#                                                                     stream_label="userData Bob")

# arr_stream_id = binance_websocket_api_manager.create_stream(arr_channels, "arr", stream_label="arr channels",
#                                                             ping_interval=10, ping_timeout=10, close_timeout=5)

alts = binance_websocket_api_manager.create_stream('channels','alt_markets',stream_label='altbtc')
btc = binance_websocket_api_manager.create_stream('channels','btcusdt',stream_label='btc')
# divisor = math.ceil(len(markets) / binance_websocket_api_manager.get_limit_of_subscriptions_per_stream())
# max_subscriptions = math.ceil(len(markets) / divisor)

# for channel in channels:
#     if len(markets) <= max_subscriptions:
#         binance_websocket_api_manager.create_stream(channel, markets, stream_label=channel)
#     else:
#         loops = 1
#         i = 1
#         markets_sub = []
#         for market in markets:
#             markets_sub.append(market)
#             if i == max_subscriptions or loops*max_subscriptions + i == len(markets):
#                 binance_websocket_api_manager.create_stream(channel, markets_sub, stream_label=str(channel+"_"+str(i)),
#                                                             ping_interval=10, ping_timeout=10, close_timeout=5)
#                 markets_sub = []
#                 i = 1
#                 loops += 1
#             i += 1

while True:
    binance_websocket_api_manager.print_summary()
    #binance_websocket_api_manager.print_stream_info(arr_stream_id)
    time.sleep(5)