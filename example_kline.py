from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import logging
import time
import os


# https://docs.python.org/3/library/logging.html#logging-levels
logging.basicConfig(level=logging.ERROR,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

# create instance of BinanceWebSocketApiManager
binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com", output_default="UnicornFy")

markets = {'xrpbtc'}

binance_websocket_api_manager.create_stream('kline_1m', markets, stream_label="UnicornFy", output="UnicornFy")

binance_websocket_api_manager.create_stream('kline_1m', markets, stream_label="dict", output="dict")

binance_websocket_api_manager.create_stream('kline_1m', markets, stream_label="raw_data", output="raw_data")

while True:
    if binance_websocket_api_manager.is_manager_stopping():
        exit(0)
    oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
    if oldest_stream_data_from_stream_buffer is False:
        time.sleep(0.01)
    else:
        if oldest_stream_data_from_stream_buffer is not None:
            try:
                if oldest_stream_data_from_stream_buffer['event_time'] >= \
                        oldest_stream_data_from_stream_buffer['kline']['kline_close_time']:
                    # print only the last kline
                    print(f"UnicornFy: {oldest_stream_data_from_stream_buffer}")
            except KeyError:
                print(f"dict: {oldest_stream_data_from_stream_buffer}")
            except TypeError:
                print(f"raw_data: {oldest_stream_data_from_stream_buffer}")
