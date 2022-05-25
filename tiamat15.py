
from f15 import idx_array, initial_klines, watch_closed, watch_data, watch_loss

from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

import time
import threading

from binance.client import Client
from binance.enums import *



apikey = 'Ems0rvjDxU18jreN85LUDKZGZ65L0vEf6n3jPoYpwMH3o6rOHjGxNQ13axAtzRWh '
secretkey = 'He1BSM3zuHUrdyQxFEtKVhhPEZtwaTFQ6TE1pDjSskSv1YtK2WbBanqpyKYJoHFt'

client = Client(apikey,secretkey)


markets = ['scusdt','thetausdt','bchusdt','dashusdt','snxusdt','wnxmusdt','xtzusdt','firousdt','zecusdt','ontusdt']

channels = ['kline_1m']

market_caps7 = ['SCUSDT']
market_caps8 = ['THETAUSDT']
market_caps9 = ['BCHUSDT']
market_caps10 = ['DASHUSDT']
market_caps11 = ['SNXUSDT']
market_caps12 = ['WNXMUSDT']
market_caps13 = ['XTZUSDT']
market_caps14 = ['FIROUSDT']
market_caps15 = ['ZECUSDT']
market_caps16 = ['ONTUSDT']



mrkt7 = 'SCUSDT'
symbol7 = 'SC'
dec7 = 0    
price_limit_dec7 = 6    

mrkt8 = 'THETAUSDT'
symbol8 = 'THETA'
dec8 = 1
price_limit_dec8 = 5

mrkt9 = 'BCHUSDT'
symbol9 = 'BCH'
dec9 = 5
price_limit_dec9 = 2

mrkt10 = 'DASHUSDT'
symbol10 = 'DASH'
dec10 = 5
price_limit_dec10 = 2

mrkt11 = 'SNXUSDT'
symbol11 = 'SNX'
dec11 = 3
price_limit_dec11 = 3

mrkt12 = 'WNXMUSDT'
symbol12 = 'WNXM'
dec12 = 3
price_limit_dec12 = 3

mrkt13 = 'XTZUSDT'
symbol13 = 'XTZ'
dec13 = 2
price_limit_dec13 = 4

mrkt14 = 'FIROUSDT'
symbol14 = 'FIRO'
dec14 = 3
price_limit_dec14 = 3

mrkt15 = 'ZECUSDT'
symbol15 = 'ZEC'
dec15 = 5
price_limit_dec15 = 2 

mrkt16 = 'ONTUSDT'
symbol16 = 'ONT'
dec16 = 2
price_limit_dec16 = 4


latest_klines7 = initial_klines(market_caps7)
latest_closed7 = idx_array(latest_klines7,4)

latest_klines8 = initial_klines(market_caps8)
latest_closed8 = idx_array(latest_klines8,4)

latest_klines9 = initial_klines(market_caps9)
latest_closed9 = idx_array(latest_klines9,4)

latest_klines10 = initial_klines(market_caps10)
latest_closed10 = idx_array(latest_klines10,4)

latest_klines11 = initial_klines(market_caps11)
latest_closed11 = idx_array(latest_klines11,4)

latest_klines12 = initial_klines(market_caps12)
latest_closed12 = idx_array(latest_klines12,4)

latest_klines13 = initial_klines(market_caps13)
latest_closed13 = idx_array(latest_klines13,4)

latest_klines14 = initial_klines(market_caps14)
latest_closed14 = idx_array(latest_klines14,4)

latest_klines15 = initial_klines(market_caps15)
latest_closed15 = idx_array(latest_klines15,4)

latest_klines16 = initial_klines(market_caps16)
latest_closed16 = idx_array(latest_klines16,4)

ma2007 = []
ma507 = []
atr157 = []

ma2008 = []
ma508 = []
atr158 = []

ma2009 = []
ma509 = []
atr159 = []

ma20010 = []
ma5010 = []
atr1510 = []

ma20011 = []
ma5011 = []
atr1511 = []

ma20012 = []
ma5012 = []
atr1512 = []

ma20013 = []
ma5013 = []
atr1513 = []

ma20014 = []
ma5014 = []
atr1514 = []

ma20015 = []
ma5015 = []
atr1515 = []

ma20016 = []
ma5016 = []
atr1516 = []


rsi147 = []
bullish7 = []

rsi148 = []
bullish8 = []

rsi149 = []
bullish9 = []

rsi1410 = []
bullish10 = []

rsi1411 = []
bullish11 = []

rsi1412 = []
bullish12 = []

rsi1413 = []
bullish13 = []

rsi1414 = []
bullish14 = []

rsi1415 = []
bullish15 = []

rsi1416 = []
bullish16 = []


buffer_candle_unclosed7 = []
buffer_candle_closed7 = []

buffer_candle_unclosed8 = []
buffer_candle_closed8 = []

buffer_candle_unclosed9 = []
buffer_candle_closed9 = []

buffer_candle_unclosed10 = []
buffer_candle_closed10 = []

buffer_candle_unclosed11 = []
buffer_candle_closed11 = []

buffer_candle_unclosed12 = []
buffer_candle_closed12 = []

buffer_candle_unclosed13 = []
buffer_candle_closed13 = []

buffer_candle_unclosed14 = []
buffer_candle_closed14 = []

buffer_candle_unclosed15 = []
buffer_candle_closed15 = []

buffer_candle_unclosed16 = []
buffer_candle_closed16 = []


ctr7 = []
retries7 = []

ctr8 = []
retries8 = []

ctr9 = []
retries9 = []

ctr10 = []
retries10 = []

ctr11 = []
retries11 = []

ctr12 = []
retries12 = []

ctr13 = []
retries13 = []

ctr14 = []
retries14 = []

ctr15 = []
retries15 = []

ctr16 = []
retries16 = []


stoploss7 = []
order7 = []

stoploss8 = []
order8 = []

stoploss9 = []
order9 = []

stoploss10 = []
order10 = []

stoploss11 = []
order11 = []

stoploss12 = []
order12 = []

stoploss13 = []
order13 = []

stoploss14 = []
order14 = []

stoploss15 = []
order15 = []

stoploss16 = []
order16 = []

rsi_counter7 = []
rsi_counter8 = []
rsi_counter9 = []
rsi_counter10 = []
rsi_counter11 = []
rsi_counter12 = []
rsi_counter13 = []
rsi_counter14 = []
rsi_counter15 = []
rsi_counter16 = []


loss_streak = []



def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            try:
                symbol = oldest_stream_data_from_stream_buffer['data']['k']['s']
                is_it_closed = oldest_stream_data_from_stream_buffer['data']['k']['x']

                if symbol == mrkt7:
                    if is_it_closed == False:              
                        buffer_candle_unclosed7.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed7.append(oldest_stream_data_from_stream_buffer)
                         

                elif symbol == mrkt8:
                    if is_it_closed == False:              
                        buffer_candle_unclosed8.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed8.append(oldest_stream_data_from_stream_buffer)
                        
                        
                elif symbol == mrkt9:
                    if is_it_closed == False:              
                        buffer_candle_unclosed9.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed9.append(oldest_stream_data_from_stream_buffer)
                                                

                elif symbol == mrkt10:
                    if is_it_closed == False:              
                        buffer_candle_unclosed10.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed10.append(oldest_stream_data_from_stream_buffer)

                elif symbol == mrkt11:
                    if is_it_closed == False:              
                        buffer_candle_unclosed11.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed11.append(oldest_stream_data_from_stream_buffer)

                elif symbol == mrkt12:
                    if is_it_closed == False:              
                        buffer_candle_unclosed12.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed12.append(oldest_stream_data_from_stream_buffer)

                elif symbol == mrkt13:
                    if is_it_closed == False:              
                        buffer_candle_unclosed13.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed13.append(oldest_stream_data_from_stream_buffer)

                elif symbol == mrkt14:
                    if is_it_closed == False:              
                        buffer_candle_unclosed14.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed14.append(oldest_stream_data_from_stream_buffer)

                elif symbol == mrkt15:
                    if is_it_closed == False:              
                        buffer_candle_unclosed15.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed15.append(oldest_stream_data_from_stream_buffer)

                elif symbol == mrkt16:
                    if is_it_closed == False:              
                        buffer_candle_unclosed16.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed16.append(oldest_stream_data_from_stream_buffer)

            except Exception:
                # not able to process the data? write it back to the stream_buffer
                binance_websocket_api_manager.add_to_stream_buffer(oldest_stream_data_from_stream_buffer)
            



 



if __name__ == '__main__':
    binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com", output_default='dict')
    worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
    worker_thread.start()
    kline_stream_id = binance_websocket_api_manager.create_stream(channels, markets)
    connected = True
    count = 0
    while connected == True:
        try:
            watch_data(buffer_candle_closed7,latest_klines7,latest_closed7,ma2007,ma507,atr157,rsi147,bullish7)
            watch_data(buffer_candle_closed8,latest_klines8,latest_closed8,ma2008,ma508,atr158,rsi148,bullish8)
            watch_data(buffer_candle_closed9,latest_klines9,latest_closed9,ma2009,ma509,atr159,rsi149,bullish9)
            watch_data(buffer_candle_closed10,latest_klines10,latest_closed10,ma20010,ma5010,atr1510,rsi1410,bullish10)
            watch_data(buffer_candle_closed11,latest_klines11,latest_closed11,ma20011,ma5011,atr1511,rsi1411,bullish11)
            watch_data(buffer_candle_closed12,latest_klines12,latest_closed12,ma20012,ma5012,atr1512,rsi1412,bullish12)
            watch_data(buffer_candle_closed13,latest_klines13,latest_closed13,ma20013,ma5013,atr1513,rsi1413,bullish13)
            watch_data(buffer_candle_closed14,latest_klines14,latest_closed14,ma20014,ma5014,atr1514,rsi1414,bullish14)
            watch_data(buffer_candle_closed15,latest_klines15,latest_closed15,ma20015,ma5015,atr1515,rsi1415,bullish15)
            watch_data(buffer_candle_closed16,latest_klines16,latest_closed16,ma20016,ma5016,atr1516,rsi1416,bullish16)


            watch_loss(stoploss7,symbol7,mrkt7,dec7,buffer_candle_unclosed7,order7,loss_streak)
            watch_loss(stoploss8,symbol8,mrkt8,dec8,buffer_candle_unclosed8,order8,loss_streak) 
            watch_loss(stoploss9,symbol9,mrkt9,dec9,buffer_candle_unclosed9,order9,loss_streak)
            watch_loss(stoploss10,symbol10,mrkt10,dec10,buffer_candle_unclosed10,order10,loss_streak) 
            watch_loss(stoploss11,symbol11,mrkt11,dec11,buffer_candle_unclosed11,order11,loss_streak) 
            watch_loss(stoploss12,symbol12,mrkt12,dec12,buffer_candle_unclosed12,order12,loss_streak) 
            watch_loss(stoploss13,symbol13,mrkt13,dec13,buffer_candle_unclosed13,order13,loss_streak) 
            watch_loss(stoploss14,symbol14,mrkt14,dec14,buffer_candle_unclosed14,order14,loss_streak) 
            watch_loss(stoploss15,symbol15,mrkt15,dec15,buffer_candle_unclosed15,order15,loss_streak) 
            watch_loss(stoploss16,symbol16,mrkt16,dec16,buffer_candle_unclosed16,order16,loss_streak)
            

            watch_closed(ma2007,ma507,atr157,rsi147,buffer_candle_closed7,ctr7,retries7,stoploss7,bullish7,mrkt7,symbol7,dec7,order7,price_limit_dec7,rsi_counter7,loss_streak)
            watch_closed(ma2008,ma508,atr158,rsi148,buffer_candle_closed8,ctr8,retries8,stoploss8,bullish8,mrkt8,symbol8,dec8,order8,price_limit_dec8,rsi_counter8,loss_streak)
            watch_closed(ma2009,ma509,atr159,rsi149,buffer_candle_closed9,ctr9,retries9,stoploss9,bullish9,mrkt9,symbol9,dec9,order9,price_limit_dec9,rsi_counter9,loss_streak)
            watch_closed(ma20010,ma5010,atr1510,rsi1410,buffer_candle_closed10,ctr10,retries10,stoploss10,bullish10,mrkt10,symbol10,dec10,order10,price_limit_dec10,rsi_counter10,loss_streak)
            watch_closed(ma20011,ma5011,atr1511,rsi1411,buffer_candle_closed11,ctr11,retries11,stoploss11,bullish11,mrkt11,symbol11,dec11,order11,price_limit_dec11,rsi_counter11,loss_streak)
            watch_closed(ma20012,ma5012,atr1512,rsi1412,buffer_candle_closed12,ctr12,retries12,stoploss12,bullish12,mrkt12,symbol12,dec12,order12,price_limit_dec12,rsi_counter12,loss_streak)
            watch_closed(ma20013,ma5013,atr1513,rsi1413,buffer_candle_closed13,ctr13,retries13,stoploss13,bullish13,mrkt13,symbol13,dec13,order13,price_limit_dec13,rsi_counter13,loss_streak)
            watch_closed(ma20014,ma5014,atr1514,rsi1414,buffer_candle_closed14,ctr14,retries14,stoploss14,bullish14,mrkt14,symbol14,dec14,order14,price_limit_dec14,rsi_counter14,loss_streak)
            watch_closed(ma20015,ma5015,atr1515,rsi1415,buffer_candle_closed15,ctr15,retries15,stoploss15,bullish15,mrkt15,symbol15,dec15,order15,price_limit_dec15,rsi_counter15,loss_streak)
            watch_closed(ma20016,ma5016,atr1516,rsi1416,buffer_candle_closed16,ctr16,retries16,stoploss16,bullish16,mrkt16,symbol16,dec16,order16,price_limit_dec16,rsi_counter16,loss_streak)
            
            time.sleep(0.5)


        except KeyboardInterrupt:
            connected = False
            print("\nStopping ... just wait a few seconds!")
        except:
            if count == 3:
                connected = False
            else:
                count += 1
                time.sleep(5)
    # try:
    #     while True:
    
        

