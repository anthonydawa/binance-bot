from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

import time
import threading
import parse_data_from_stream

channels = {'trade'}
markets = {'bnbusdt'}
tt = []

def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        tt.append(oldest_stream_data_from_stream_buffer)
        print(tt)
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            try:
                parse_data_from_stream.parse_data_from_stream(oldest_stream_data_from_stream_buffer)
            except Exception:
                # not able to process the data? write it back to the stream_buffer
                binance_websocket_api_manager.add_to_stream_buffer(oldest_stream_data_from_stream_buffer)
            


if __name__ == '__main__':
    binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com")
    worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
    worker_thread.start()
    kline_stream_id = binance_websocket_api_manager.create_stream(channels, markets)
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nStopping ... just wait a few seconds!")
        binance_websocket_api_manager.stop_manager_with_all_streams()