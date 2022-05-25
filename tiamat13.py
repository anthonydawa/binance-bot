
from f12 import idx_array, initial_klines, watch_closed, watch_data, watch_loss

from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

import time
import threading

from binance.client import Client
from binance.enums import *



apikey = '00wFV02rJrMKJqV5w3X8JwqmdnH1FKqrFKDnmajBZp9FweqZ79H48eOqjJ8mk54t'
secretkey = '1HbwIs0BUUbtvgDpOzgTFAz1EsAT6e7dFTZNNpVUwyTVrb1biKjynwTThhtzmDhf'
client = Client(apikey,secretkey)




markets = ['nknusdt','ardrusdt','viteusdt','epsusdt','iostusdt','wavesusdt','mdtusdt','zrxusdt','cakeusdt','filusdt']

channels = ['kline_1m']

market_caps = ['NKNUSDT']
market_caps2 = ['ARDRUSDT']
market_caps3 = ['VITEUSDT']
market_caps4 = ['EPSUSDT']
market_caps5 = ['IOSTUSDT']
market_caps6 = ['WAVESUSDT']
market_caps7 = ['MDTUSDT']
market_caps8 = ['ZRXUSDT']
market_caps9 = ['CAKEUSDT']
market_caps10 = ['FILUSDT']


mrkt = 'NKNUSDT'
symbol = 'NKN'
dec = 1
price_limit_dec = 5

mrkt2 = 'ARDRUSDT'
symbol2 = 'ARDR'
dec2 = 1
price_limit_dec2 = 5

mrkt3 = 'VITEUSDT'
symbol3 = 'VITE'
dec3 = 1
price_limit_dec3 = 5

mrkt4 = 'EPSUSDT'
symbol4 = 'EPS'
dec4 = 3
price_limit_dec4 = 3

mrkt5 = 'IOSTUSDT'
symbol5 = 'IOST'
dec5 = 0
price_limit_dec5 = 6

mrkt6 = 'WAVESUSDT'
symbol6 = 'WAVES'
dec6 = 2
price_limit_dec6 = 4

mrkt7 = 'MDTUSDT'
symbol7 = 'MDT'
dec7 = 1
price_limit_dec7 = 5

mrkt8 = 'ZRXUSDT'
symbol8 = 'ZRX'
dec8 = 2
price_limit_dec8 = 4

mrkt9 = 'CAKEUSDT'
symbol9 = 'CAKE'
dec9 = 3
price_limit_dec9 = 3

mrkt10 = 'FILUSDT'
symbol10 = 'FIL'
dec10 = 2
price_limit_dec10 = 4


latest_klines = initial_klines(market_caps)
latest_closed = idx_array(latest_klines,4)
# latest_200ma = ExpMa(latest_closed,200)
# latest_50ma = ExpMa(latest_closed[-55:],50)
# latest_atr = AverageTrueRange(latest_klines)

latest_klines2 = initial_klines(market_caps2)
latest_closed2 = idx_array(latest_klines2,4)

latest_klines3 = initial_klines(market_caps3)
latest_closed3 = idx_array(latest_klines3,4)

latest_klines4 = initial_klines(market_caps4)
latest_closed4 = idx_array(latest_klines4,4)

latest_klines5 = initial_klines(market_caps5)
latest_closed5 = idx_array(latest_klines5,4)

latest_klines6 = initial_klines(market_caps6)
latest_closed6 = idx_array(latest_klines6,4)

latest_klines7 = initial_klines(market_caps7)
latest_closed7 = idx_array(latest_klines7,4)

latest_klines8 = initial_klines(market_caps8)
latest_closed8 = idx_array(latest_klines8,4)

latest_klines9 = initial_klines(market_caps9)
latest_closed9 = idx_array(latest_klines9,4)

latest_klines10 = initial_klines(market_caps10)
latest_closed10 = idx_array(latest_klines10,4)


ma200 = []
ma50 = []
atr15 = []

ma2002 = []
ma502 = []
atr152 = []

ma2003 = []
ma503 = []
atr153 = []

ma2004 = []
ma504 = []
atr154 = []

ma2005 = []
ma505 = []
atr155 = []

ma2006 = []
ma506 = []
atr156 = []

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

rsi14 = []
bullish = []

rsi142 = []
bullish2 = []

rsi143 = []
bullish3 = []

rsi144 = []
bullish4 = []

rsi145 = []
bullish5 = []

rsi146 = []
bullish6 = []

rsi147 = []
bullish7 = []

rsi148 = []
bullish8 = []

rsi149 = []
bullish9 = []

rsi1410 = []
bullish10 = []


buffer_candle_unclosed = []
buffer_candle_closed = []

buffer_candle_unclosed2 = []
buffer_candle_closed2 = []

buffer_candle_unclosed3 = []
buffer_candle_closed3 = []

buffer_candle_unclosed4 = []
buffer_candle_closed4 = []

buffer_candle_unclosed5 = []
buffer_candle_closed5 = []

buffer_candle_unclosed6 = []
buffer_candle_closed6 = []

buffer_candle_unclosed7 = []
buffer_candle_closed7 = []

buffer_candle_unclosed8 = []
buffer_candle_closed8 = []

buffer_candle_unclosed9 = []
buffer_candle_closed9 = []

buffer_candle_unclosed10 = []
buffer_candle_closed10 = []

ctr = []
retries = []

ctr2 = []
retries2 = []

ctr3 = []
retries3 = []

ctr4 = []
retries4 = []

ctr5 = []
retries5 = []

ctr6 = []
retries6 = []

ctr7 = []
retries7 = []

ctr8 = []
retries8 = []

ctr9 = []
retries9 = []

ctr10 = []
retries10 = []


stoploss = []
order = []

stoploss2 = []
order2 = []

stoploss3 = []
order3 = []

stoploss4 = []
order4 = []

stoploss5 = []
order5 = []

stoploss6 = []
order6 = []

stoploss7 = []
order7 = []

stoploss8 = []
order8 = []


stoploss9 = []
order9 = []

stoploss10 = []
order10 = []


rsi_counter = []
rsi_counter2 = []
rsi_counter3 = []
rsi_counter4 = []
rsi_counter5 = []
rsi_counter6 = []
rsi_counter7 = []
rsi_counter8 = []
rsi_counter9 = []
rsi_counter10 = []


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

                if symbol == mrkt:
                    if is_it_closed == False:              
                        buffer_candle_unclosed.append(oldest_stream_data_from_stream_buffer)

                        
                    elif is_it_closed == True:
                        buffer_candle_closed.append(oldest_stream_data_from_stream_buffer)


                elif symbol == mrkt2:
                    if is_it_closed == False:              
                        buffer_candle_unclosed2.append(oldest_stream_data_from_stream_buffer)
                        
                    elif is_it_closed == True:
                        buffer_candle_closed2.append(oldest_stream_data_from_stream_buffer)


                elif symbol == mrkt3:
                    if is_it_closed == False:              
                        buffer_candle_unclosed3.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed3.append(oldest_stream_data_from_stream_buffer)
                        
                        
                elif symbol == mrkt4:
                    if is_it_closed == False:              
                        buffer_candle_unclosed4.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed4.append(oldest_stream_data_from_stream_buffer)
                           

                elif symbol == mrkt5:
                    if is_it_closed == False:              
                        buffer_candle_unclosed5.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed5.append(oldest_stream_data_from_stream_buffer)
                         

                elif symbol == mrkt6:
                    if is_it_closed == False:              
                        buffer_candle_unclosed6.append(oldest_stream_data_from_stream_buffer)
                        
                        
                    elif is_it_closed == True:
                        buffer_candle_closed6.append(oldest_stream_data_from_stream_buffer)
                           

                elif symbol == mrkt7:
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


            except Exception:
                # not able to process the data? write it back to the stream_buffer
                binance_websocket_api_manager.add_to_stream_buffer(oldest_stream_data_from_stream_buffer)
            



def all_watch_data():
    while True:
        watch_data(buffer_candle_closed,latest_klines,latest_closed,ma200,ma50,atr15,rsi14,bullish)
        watch_data(buffer_candle_closed2,latest_klines2,latest_closed2,ma2002,ma502,atr152,rsi142,bullish2)
        watch_data(buffer_candle_closed3,latest_klines3,latest_closed3,ma2003,ma503,atr153,rsi143,bullish3)
        watch_data(buffer_candle_closed4,latest_klines4,latest_closed4,ma2004,ma504,atr154,rsi144,bullish4)
        watch_data(buffer_candle_closed5,latest_klines5,latest_closed5,ma2005,ma505,atr155,rsi145,bullish5)
        watch_data(buffer_candle_closed6,latest_klines6,latest_closed6,ma2006,ma506,atr156,rsi146,bullish6)
        watch_data(buffer_candle_closed7,latest_klines7,latest_closed7,ma2007,ma507,atr157,rsi147,bullish7)
        watch_data(buffer_candle_closed8,latest_klines8,latest_closed8,ma2008,ma508,atr158,rsi148,bullish8)
        watch_data(buffer_candle_closed9,latest_klines9,latest_closed9,ma2009,ma509,atr159,rsi149,bullish9)
        watch_data(buffer_candle_closed10,latest_klines10,latest_closed10,ma20010,ma5010,atr1510,rsi1410,bullish10)
        time.sleep(0.5)

def all_watch_loss():
    while True:
        watch_loss(stoploss,symbol,mrkt,dec,buffer_candle_unclosed,order,loss_streak)
        watch_loss(stoploss2,symbol2,mrkt2,dec2,buffer_candle_unclosed2,order2,loss_streak)
        watch_loss(stoploss3,symbol3,mrkt3,dec3,buffer_candle_unclosed3,order3,loss_streak)
        watch_loss(stoploss4,symbol4,mrkt4,dec4,buffer_candle_unclosed4,order4,loss_streak) 
        watch_loss(stoploss5,symbol5,mrkt5,dec5,buffer_candle_unclosed5,order5,loss_streak)
        watch_loss(stoploss6,symbol6,mrkt6,dec6,buffer_candle_unclosed6,order6,loss_streak) 
        watch_loss(stoploss7,symbol7,mrkt7,dec7,buffer_candle_unclosed7,order7,loss_streak)
        watch_loss(stoploss8,symbol8,mrkt8,dec8,buffer_candle_unclosed8,order8,loss_streak) 
        watch_loss(stoploss9,symbol9,mrkt9,dec9,buffer_candle_unclosed9,order9,loss_streak)
        watch_loss(stoploss10,symbol10,mrkt10,dec10,buffer_candle_unclosed10,order10,loss_streak) 
        time.sleep(0.5)

def all_watch_closed():
    while True:
        watch_closed(ma200,ma50,atr15,rsi14,buffer_candle_closed,ctr,retries,stoploss,bullish,mrkt,symbol,dec,order,price_limit_dec,rsi_counter,loss_streak)
        watch_closed(ma2002,ma502,atr152,rsi142,buffer_candle_closed2,ctr2,retries2,stoploss2,bullish2,mrkt2,symbol2,dec2,order2,price_limit_dec2,rsi_counter2,loss_streak)
        watch_closed(ma2003,ma503,atr153,rsi143,buffer_candle_closed3,ctr3,retries3,stoploss3,bullish3,mrkt3,symbol3,dec3,order3,price_limit_dec3,rsi_counter3,loss_streak)
        watch_closed(ma2004,ma504,atr154,rsi144,buffer_candle_closed4,ctr4,retries4,stoploss4,bullish4,mrkt4,symbol4,dec4,order4,price_limit_dec4,rsi_counter4,loss_streak)
        watch_closed(ma2005,ma505,atr155,rsi145,buffer_candle_closed5,ctr5,retries5,stoploss5,bullish5,mrkt5,symbol5,dec5,order5,price_limit_dec5,rsi_counter5,loss_streak)
        watch_closed(ma2006,ma506,atr156,rsi146,buffer_candle_closed6,ctr6,retries6,stoploss6,bullish6,mrkt6,symbol6,dec6,order6,price_limit_dec6,rsi_counter6,loss_streak)
        watch_closed(ma2007,ma507,atr157,rsi147,buffer_candle_closed7,ctr7,retries7,stoploss7,bullish7,mrkt7,symbol7,dec7,order7,price_limit_dec7,rsi_counter7,loss_streak)
        watch_closed(ma2008,ma508,atr158,rsi148,buffer_candle_closed8,ctr8,retries8,stoploss8,bullish8,mrkt8,symbol8,dec8,order8,price_limit_dec8,rsi_counter8,loss_streak)
        watch_closed(ma2009,ma509,atr159,rsi149,buffer_candle_closed9,ctr9,retries9,stoploss9,bullish9,mrkt9,symbol9,dec9,order9,price_limit_dec9,rsi_counter9,loss_streak)
        watch_closed(ma20010,ma5010,atr1510,rsi1410,buffer_candle_closed10,ctr10,retries10,stoploss10,bullish10,mrkt10,symbol10,dec10,order10,price_limit_dec10,rsi_counter10,loss_streak)
        time.sleep(0.5)

if __name__ == '__main__':
    binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com", output_default='dict')
    worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
    worker_thread.start()
    # t1 = threading.Thread(target=all_watch_data)
    # t1.start()
    # t2 = threading.Thread(target=all_watch_loss)
    # t2.start()
    # t3 = threading.Thread(target=all_watch_closed)
    # t3.start()
    kline_stream_id = binance_websocket_api_manager.create_stream(channels, markets)
    connected = True
    count = 0
    while connected == True:
        try:
            watch_data(buffer_candle_closed,latest_klines,latest_closed,ma200,ma50,atr15,rsi14,bullish)
            watch_data(buffer_candle_closed2,latest_klines2,latest_closed2,ma2002,ma502,atr152,rsi142,bullish2)
            watch_data(buffer_candle_closed3,latest_klines3,latest_closed3,ma2003,ma503,atr153,rsi143,bullish3)
            watch_data(buffer_candle_closed4,latest_klines4,latest_closed4,ma2004,ma504,atr154,rsi144,bullish4)
            watch_data(buffer_candle_closed5,latest_klines5,latest_closed5,ma2005,ma505,atr155,rsi145,bullish5)
            watch_data(buffer_candle_closed6,latest_klines6,latest_closed6,ma2006,ma506,atr156,rsi146,bullish6)
            watch_data(buffer_candle_closed7,latest_klines7,latest_closed7,ma2007,ma507,atr157,rsi147,bullish7)
            watch_data(buffer_candle_closed8,latest_klines8,latest_closed8,ma2008,ma508,atr158,rsi148,bullish8)
            watch_data(buffer_candle_closed9,latest_klines9,latest_closed9,ma2009,ma509,atr159,rsi149,bullish9)
            watch_data(buffer_candle_closed10,latest_klines10,latest_closed10,ma20010,ma5010,atr1510,rsi1410,bullish10)



            watch_loss(stoploss,symbol,mrkt,dec,buffer_candle_unclosed,order,loss_streak)
            watch_loss(stoploss2,symbol2,mrkt2,dec2,buffer_candle_unclosed2,order2,loss_streak)
            watch_loss(stoploss3,symbol3,mrkt3,dec3,buffer_candle_unclosed3,order3,loss_streak)
            watch_loss(stoploss4,symbol4,mrkt4,dec4,buffer_candle_unclosed4,order4,loss_streak) 
            watch_loss(stoploss5,symbol5,mrkt5,dec5,buffer_candle_unclosed5,order5,loss_streak)
            watch_loss(stoploss6,symbol6,mrkt6,dec6,buffer_candle_unclosed6,order6,loss_streak) 
            watch_loss(stoploss7,symbol7,mrkt7,dec7,buffer_candle_unclosed7,order7,loss_streak)
            watch_loss(stoploss8,symbol8,mrkt8,dec8,buffer_candle_unclosed8,order8,loss_streak) 
            watch_loss(stoploss9,symbol9,mrkt9,dec9,buffer_candle_unclosed9,order9,loss_streak)
            watch_loss(stoploss10,symbol10,mrkt10,dec10,buffer_candle_unclosed10,order10,loss_streak) 
      
            
            
            watch_closed(ma200,ma50,atr15,rsi14,buffer_candle_closed,ctr,retries,stoploss,bullish,mrkt,symbol,dec,order,price_limit_dec,rsi_counter,loss_streak)
            watch_closed(ma2002,ma502,atr152,rsi142,buffer_candle_closed2,ctr2,retries2,stoploss2,bullish2,mrkt2,symbol2,dec2,order2,price_limit_dec2,rsi_counter2,loss_streak)
            watch_closed(ma2003,ma503,atr153,rsi143,buffer_candle_closed3,ctr3,retries3,stoploss3,bullish3,mrkt3,symbol3,dec3,order3,price_limit_dec3,rsi_counter3,loss_streak)
            watch_closed(ma2004,ma504,atr154,rsi144,buffer_candle_closed4,ctr4,retries4,stoploss4,bullish4,mrkt4,symbol4,dec4,order4,price_limit_dec4,rsi_counter4,loss_streak)
            watch_closed(ma2005,ma505,atr155,rsi145,buffer_candle_closed5,ctr5,retries5,stoploss5,bullish5,mrkt5,symbol5,dec5,order5,price_limit_dec5,rsi_counter5,loss_streak)
            watch_closed(ma2006,ma506,atr156,rsi146,buffer_candle_closed6,ctr6,retries6,stoploss6,bullish6,mrkt6,symbol6,dec6,order6,price_limit_dec6,rsi_counter6,loss_streak)
            watch_closed(ma2007,ma507,atr157,rsi147,buffer_candle_closed7,ctr7,retries7,stoploss7,bullish7,mrkt7,symbol7,dec7,order7,price_limit_dec7,rsi_counter7,loss_streak)
            watch_closed(ma2008,ma508,atr158,rsi148,buffer_candle_closed8,ctr8,retries8,stoploss8,bullish8,mrkt8,symbol8,dec8,order8,price_limit_dec8,rsi_counter8,loss_streak)
            watch_closed(ma2009,ma509,atr159,rsi149,buffer_candle_closed9,ctr9,retries9,stoploss9,bullish9,mrkt9,symbol9,dec9,order9,price_limit_dec9,rsi_counter9,loss_streak)
            watch_closed(ma20010,ma5010,atr1510,rsi1410,buffer_candle_closed10,ctr10,retries10,stoploss10,bullish10,mrkt10,symbol10,dec10,order10,price_limit_dec10,rsi_counter10,loss_streak)
            
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

