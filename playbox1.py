
from algov2 import AverageTrueRange, idx_array, initial_klines, ExpMa, watch_closed, watch_data, watch_loss
from helper_func import upper_case
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager

import time
import threading

from binance.client import Client
from binance.enums import *



apikey = 'GzzQmi4d8B6uQXd9cXyCjDn9l38ckQ8LhZHCKkDcC6zl0q0Y6hVKdb2pJBj7Etmp'
secretkey = '5PmwqijHxOekhrBSYxhox7CmEhPG7yXJWA7bbnSIWH3HQ6Z5Vf38loM5VtkgNwQb'
client = Client(apikey,secretkey)


markets = ['xrpusdt','adausdt','dotusdt','uniusdt','ltcusdt','linkusdt','bchusdt','xlmusdt','trxusdt','vetusdt','thetausdt','bttusdt','eosusdt','enjusdt','chzusdt','hotusdt']

channels = ['kline_5m']

market_caps = ['XRPUSDT']
market_caps2 = ['ADAUSDT']
market_caps3 = ['DOTUSDT']
market_caps4 = ['UNIUSDT']
market_caps5 = ['LTCUSDT']
market_caps6 = ['LINKUSDT']
market_caps7 = ['BCHUSDT']
market_caps8 = ['XLMUSDT']
market_caps9 = ['TRXUSDT']
market_caps10 = ['VETUSDT']
market_caps11 = ['THETAUSDT']
market_caps12 = ['BTTUSDT']
market_caps13 = ['EOSUSDT']
market_caps14 = ['ENJUSDT']
market_caps15 = ['CHZUSDT']
market_caps16 = ['HOTUSDT']

mrkt = 'XRPUSDT'
symbol = 'XRP'
dec = 1
price_limit_dec = 5

mrkt2 = 'ADAUSDT'
symbol2 = 'ADA'
dec2 = 1
price_limit_dec2 = 5

mrkt3 = 'DOTUSDT'
symbol3 = 'DOT'
dec3 = 2
price_limit_dec3 = 4

mrkt4 = 'UNIUSDT'
symbol4 = 'UNI'
dec4 = 2
price_limit_dec4 = 4

mrkt5 = 'LTCUSDT'
symbol5 = 'LTC'
dec5 = 5
price_limit_dec5 = 2

mrkt6 = 'LINKUSDT'
symbol6 = 'LINK'
dec6 = 2
price_limit_dec6 = 4

mrkt7 = 'BCHUSDT'
symbol7 = 'BCH'
dec7 = 5
price_limit_dec7 = 2

mrkt8 = 'XLMUSDT'
symbol8 = 'XLM'
dec8 = 1
price_limit_dec8 = 5

mrkt9 = 'TRXUSDT'
symbol9 = 'TRX'
dec9 = 1
price_limit_dec9 = 5

mrkt10 = 'VETUSDT'
symbol10 = 'VET'
dec10 = 0
price_limit_dec10 = 6

mrkt11 = 'THETAUSDT'
symbol11 = 'THETA'
dec11 = 1
price_limit_dec11 = 5

mrkt12 = 'BTTUSDT'
symbol12 = 'BTT'
dec12 = 0
price_limit_dec12 = 7

mrkt13 = 'EOSUSDT'
symbol13 = 'EOS'
dec13 = 2
price_limit_dec13 = 4

mrkt14 = 'ENJUSDT'
symbol14 = 'ENJ'
dec14 = 1
price_limit_dec14 = 5

mrkt15 = 'CHZUSDT'
symbol15 = 'CHZ'
dec15 = 1
price_limit_dec15 = 5

mrkt16 = 'HOTUSDT'
symbol16 = 'HOT'
dec16 = 0
price_limit_dec16 = 7

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
    try:
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
            watch_data(buffer_candle_closed11,latest_klines11,latest_closed11,ma20011,ma5011,atr1511,rsi1411,bullish11)
            watch_data(buffer_candle_closed12,latest_klines12,latest_closed12,ma20012,ma5012,atr1512,rsi1412,bullish12)
            watch_data(buffer_candle_closed13,latest_klines13,latest_closed13,ma20013,ma5013,atr1513,rsi1413,bullish13)
            watch_data(buffer_candle_closed14,latest_klines14,latest_closed14,ma20014,ma5014,atr1514,rsi1414,bullish14)
            watch_data(buffer_candle_closed15,latest_klines15,latest_closed15,ma20015,ma5015,atr1515,rsi1415,bullish15)
            watch_data(buffer_candle_closed16,latest_klines16,latest_closed16,ma20016,ma5016,atr1516,rsi1416,bullish16)


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
            watch_loss(stoploss11,symbol11,mrkt11,dec11,buffer_candle_unclosed11,order11,loss_streak) 
            watch_loss(stoploss12,symbol12,mrkt12,dec12,buffer_candle_unclosed12,order12,loss_streak) 
            watch_loss(stoploss13,symbol13,mrkt13,dec13,buffer_candle_unclosed13,order13,loss_streak) 
            watch_loss(stoploss14,symbol14,mrkt14,dec14,buffer_candle_unclosed14,order14,loss_streak) 
            watch_loss(stoploss15,symbol15,mrkt15,dec15,buffer_candle_unclosed15,order15,loss_streak) 
            watch_loss(stoploss16,symbol16,mrkt16,dec16,buffer_candle_unclosed16,order16,loss_streak)
            
            
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
            watch_closed(ma20011,ma5011,atr1511,rsi1411,buffer_candle_closed11,ctr11,retries11,stoploss11,bullish11,mrkt11,symbol11,dec11,order11,price_limit_dec11,rsi_counter11,loss_streak)
            watch_closed(ma20012,ma5012,atr1512,rsi1412,buffer_candle_closed12,ctr12,retries12,stoploss12,bullish12,mrkt12,symbol12,dec12,order12,price_limit_dec12,rsi_counter12,loss_streak)
            watch_closed(ma20013,ma5013,atr1513,rsi1413,buffer_candle_closed13,ctr13,retries13,stoploss13,bullish13,mrkt13,symbol13,dec13,order13,price_limit_dec13,rsi_counter13,loss_streak)
            watch_closed(ma20014,ma5014,atr1514,rsi1414,buffer_candle_closed14,ctr14,retries14,stoploss14,bullish14,mrkt14,symbol14,dec14,order14,price_limit_dec14,rsi_counter14,loss_streak)
            watch_closed(ma20015,ma5015,atr1515,rsi1415,buffer_candle_closed15,ctr15,retries15,stoploss15,bullish15,mrkt15,symbol15,dec15,order15,price_limit_dec15,rsi_counter15,loss_streak)
            watch_closed(ma20016,ma5016,atr1516,rsi1416,buffer_candle_closed16,ctr16,retries16,stoploss16,bullish16,mrkt16,symbol16,dec16,order16,price_limit_dec16,rsi_counter16,loss_streak)
            
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nStopping ... just wait a few seconds!")
        

