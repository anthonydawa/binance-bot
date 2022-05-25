from helper_func import return_incomplete_orders
from MarketProcess import MarketProcess
from MarketProces_test import MarketProcess_test
from market import get_cached_market
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

import time
import threading
from queue import Queue

from binance.client import Client
from credentials import apikey, secretkey

client = Client(apikey,secretkey)


markets = get_cached_market()[112:169]
# markets= ['btcusdt','adausdt','ethusdt','bnbusdt','ltcusdt','xrpusdt','etcusdt','dotusdt','linkusdt','trxusdt','vetusdt','bttusdt','cakeusdt','maticusdt']
# channels = ['kline_5m','kline_15m','kline_1h','kline_4h']
channels = ['kline_5m']
test_mode = True

market_objects = []

if test_mode:
    for m in markets:
        u = m.upper()
        try:
            market_objects.append(MarketProcess_test(u))
            print(u)
        except:
            pass
        time.sleep(0.1)

if not test_mode:
    for m in markets:
        u = m.upper()
        market_objects.append(MarketProcess(u))
        print(u)
        time.sleep(0.1)

    incomplete_orders = return_incomplete_orders()

    for incomplete_order in incomplete_orders:
        for market_object in market_objects:
            if incomplete_order[0] == market_object.symbol:
                market_object.active_order = incomplete_order[1]
                market_object.OrderId = [incomplete_order[2],incomplete_order[3]]


work_lock = threading.Lock()

def pool_of_jobs(worker):

    symbol = str(worker['data']['k']['s']).upper()
    closed = worker['data']['k']['x']
    
    with work_lock:
        for mrkt in market_objects:
            if symbol == mrkt.symbol:
                if closed == True:
                    mrkt.update_klines(worker)
                elif closed == False:
                    mrkt.check_price(worker)


def threader():

    while True:
        worker = q.get()
        
        pool_of_jobs(worker)

        q.task_done()

q = Queue()

for x in range(300):
    t = threading.Thread(target=threader)
    t.start()


def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            try:
                
                is_closed = oldest_stream_data_from_stream_buffer['data']['k']['x']
                # if is_closed == True:
                #     print(oldest_stream_data_from_stream_buffer)
                # if is_closed == True:
                    # print(oldest_stream_data_from_stream_buffer)
                if is_closed == True or is_closed == False:
                    q.put(oldest_stream_data_from_stream_buffer)
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
