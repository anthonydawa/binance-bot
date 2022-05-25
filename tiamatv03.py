
from atr import AverageTrueRange
from ema_init import ema_init
from helper_func import assign_new_val_and_pop, return_other_empty, shift_slide, upper_case
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

import time
import threading
import parse_data
import ema
import get_kline_history
import numpy as np

from binance.client import Client
from binance.enums import *
client = Client('vgDhGQw1VAJoB9lICjNc0sZNRIdruOBoDTIEOv6RXA265NisxvP8kEctcKu1c1Cb', '5xwAu0jnNVDiLnNsrhjAaRD6BmlRa2O9nNm3g5GlT0ByIJv74zBu4Q8RWKzOps10')




# GLOBAL VAR HERE ONLY
markets = ['adausdt','bnbusdt']
market_caps = upper_case(markets)

channels = ['kline_1m']

#200 latest candles 
init_klines = get_kline_history.initial_klines(market_caps)[:,:,:5]
init_closed_klines = init_klines[:,:,4]
init_ema_200 = ema_init(init_closed_klines,200)
init_ema_50 = ema_init(init_closed_klines,50)
init_atr = AverageTrueRange(init_klines)

place_closed_klines = []

latest_closed_klines = return_other_empty(place_closed_klines,init_klines)

buffer_candle_closed = []
buffer_candle_unclosed = []



#GET STREAM DATA HERE

def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            try:
                # print(oldest_stream_data_from_stream_buffer)
                is_it_closed = oldest_stream_data_from_stream_buffer['data']['k']['x']
                # print(is_it_closed)
                # datec = oldest_stream_data_from_stream_buffer['data']['k']['E']
                # openc = oldest_stream_data_from_stream_buffer['data']['k']['o']
                # highc = oldest_stream_data_from_stream_buffer['data']['k']['h']
                # lowc = oldest_stream_data_from_stream_buffer['data']['k']['l']
                # closec = oldest_stream_data_from_stream_buffer['data']['k']['c']
                # symbol = oldest_stream_data_from_stream_buffer['data']['k']['s']
                # kline = [datec,openc,highc,lowc,closec,symbol]

                if is_it_closed == False:
                    buffer_candle_unclosed.append(oldest_stream_data_from_stream_buffer['data'])
                    # count_unclosed.append(oldest_stream_data_from_stream_buffer['data'])
                elif is_it_closed == True:
                    print(1)
                    buffer_candle_closed.append(oldest_stream_data_from_stream_buffer['data'])
                    # count_unclosed.append(oldest_stream_data_from_stream_buffer['data'])

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
            place_closed_klines = shift_slide(buffer_candle_unclosed,market_caps,latest_closed_klines)
            # print('___________________________________________________________________________')
            # print(latest_closed_klines[0,-2:])
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nStopping ... just wait a few seconds!")
        