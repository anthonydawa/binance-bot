import time
from Candles import Candles
from market_order import buy_market_order, get_lot_size,get_price_filter, sell_limit_order,sell_market_order
from credentials import apikey, secretkey
from binance.client import Client

client = Client(apikey,secretkey)


class MarketProcess:

    def __init__(self,symbol):

        self.symbol = str(symbol).upper()
        self.kline_5m = Candles(self.symbol,'5m')
        self.kline_15m = Candles(self.symbol,'15m')
        self.kline_1h = Candles(self.symbol,'1h')
        self.kline_4h = Candles(self.symbol,'4h')
        self.lot_size = get_lot_size(self.symbol)
        self.price_filter = get_price_filter(self.symbol)
        self.active_order = None
        self.OrderId = None

    def get_last_kline(self,timeframe):
        if timeframe == '5m':
            return self.kline_5m.klines[-1]
        elif timeframe == '15m':
            return self.kline_15m.klines[-1]
        elif timeframe == '1h':
            return self.kline_1h.klines[-1]
        elif timeframe == '4h':
            return self.kline_4h.klines[-1]

    def update_klines(self,kline_from_stream):

        # start = time.time()
        
        datex = int(kline_from_stream['data']['k']['t'])
        timeframex = str(kline_from_stream['data']['k']['i'])
        closex = int(kline_from_stream['data']['k']['c'])
        
        last_kline_15m = self.get_last_kline('15m')[0]
        last_kline_1h = self.get_last_kline('1h')[0]
        last_kline_4h = self.get_last_kline('4h')[0]

        u_diff_5m = 300_000
        u_diff_15m = 900_000
        u_diff_1h = 3_600_000
        u_diff_4h = 14_400_000

        actual_time = datex + u_diff_5m

        actual_last_time_15m = last_kline_15m + u_diff_15m
        actual_last_time_1h = last_kline_1h + u_diff_1h
        actual_last_time_4h = last_kline_4h + u_diff_4h




        if timeframex == '5m':

            buy_signal = self.kline_5m.update(kline_from_stream)

            if not self.active_order and not self.OrderId:
                if buy_signal:
                    
                    buy_props = buy_signal.pop()

                    buy_market_order(self.symbol,self.lot_size)
                    my_limit_order = sell_limit_order(self.symbol,buy_props[0],self.lot_size,self.price_filter)
                    
                    self.OrderId = my_limit_order
                    self.active_order = buy_props

                    with open('data/saved_orders','a') as f:
                        f.write(f'{self.symbol},{my_limit_order},{buy_props[0]},{buy_props[1]}\n') 







############################################################################
            if u_diff_15m == (actual_time - actual_last_time_15m):
        
                
                
                buy_signal = self.kline_15m.update(kline_from_stream)

                if not self.active_order and not self.OrderId:
                    if buy_signal:
                        
                        buy_props = buy_signal.pop()

                        buy_market_order(self.symbol,self.lot_size)
                        my_limit_order = sell_limit_order(self.symbol,buy_props[0],self.lot_size,self.price_filter)
                        
                        self.OrderId = my_limit_order
                        self.active_order = buy_props
                        with open('data/saved_orders','a') as f:
                            f.write(f'{self.symbol},{my_limit_order},{buy_props[0]},{buy_props[1]}\n')
                               
############################################################################

            
            if u_diff_1h == (actual_time - actual_last_time_1h):    

                
                buy_signal = self.kline_1h.update(kline_from_stream)

                if not self.active_order and not self.OrderId:
                    if buy_signal:
                        
                        buy_props = buy_signal.pop()

                        buy_market_order(self.symbol,self.lot_size)
                        my_limit_order = sell_limit_order(self.symbol,buy_props[0],self.lot_size,self.price_filter)
                        
                        self.OrderId = my_limit_order
                        self.active_order = buy_props                
                        with open('data/saved_orders','a') as f:
                            f.write(f'{self.symbol},{my_limit_order},{buy_props[0]},{buy_props[1]}\n')   


############################################################################

            
            if u_diff_4h == (actual_time - actual_last_time_4h): 
                
                buy_signal = self.kline_4h.update(kline_from_stream)

                if not self.active_order and not self.OrderId:
                    if buy_signal:
                        
                        buy_props = buy_signal.pop()

                        buy_market_order(self.symbol,self.lot_size)
                        my_limit_order = sell_limit_order(self.symbol,buy_props[0],self.lot_size,self.price_filter)
                        
                        self.OrderId = my_limit_order
                        self.active_order = buy_props

                        with open('data/saved_orders','a') as f:
                            f.write(f'{self.symbol},{my_limit_order},{buy_props[0]},{buy_props[1]}\n') 
            

        # print(self.symbol,'@ update took', time.time()-start)

############################################################################

    def check_price(self,price_from_stream):

        start = time.time()


        if self.active_order and self.OrderId:

            highx = float(price_from_stream['data']['k']['h'])
            lowx = float(price_from_stream['data']['k']['l'])
            price = float(price_from_stream['data']['k']['c'])
            
            
            if lowx <= self.active_order[0] <= highx or price >= self.active_order[0]:

                try:
                    check_order = client.get_order(symbol=self.symbol,orderId=self.OrderId) 

                    if check_order['status'] == 'FILLED':

                        with open('data/completed_orders','a') as f:
                            f.write(f'{self.symbol},{self.OrderId},True\n')

                        self.active_order = None
                        self.OrderId = None 

                        print('sell limit order filled!')

                except:
                    print('error checking order')


            

            elif price <= self.active_order[1]:
                
                retries = 0
                while retries <= 3:
                    try:
                        client.cancel_order(symbol=self.symbol,orderId=self.OrderId)
                        sell_market_order(self.symbol,self.lot_size)

                        with open('data/completed_orders','a') as f:
                            f.write(f'{self.symbol},{self.OrderId},False\n')
                            
                        self.active_order = None
                        self.OrderId = None   
                    except:
                        retries += 1

        elif self.active_order and not self.OrderId:       
            
            try:
                sell_limit_order(self.symbol,self.active_order[0],self.lot_size,self.price_filter)
            except:
                sell_market_order(self.symbol,self.lot_size)

        print(self.symbol,'@ check price took', time.time()-start)

# market = MarketProcess('adausdt')


# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964186053, 's': 'ADAUSDT', 't': 155643451, 'p': '1.86950000', 'q': '147.60000000', 'b': 1468792461, 'a': 1468792454, 'T': 1620964186052, 'm': False, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964186074, 's': 'ADAUSDT', 't': 155643452, 'p': '1.86950000', 'q': '212.06000000', 'b': 1468792463, 'a': 1468792454, 'T': 1620964186073, 'm': False, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964186092, 's': 'ADAUSDT', 't': 155643453, 'p': '1.86960000', 'q': '1000.00000000', 'b': 1468792466, 'a': 1468792434, 'T': 1620964186092, 'm': False, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964186351, 's': 'ADAUSDT', 't': 155643454, 'p': '1.86960000', 'q': '5.99000000', 'b': 1468792505, 'a': 1468792522, 'T': 1620964186350, 'm': True, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964187258, 's': 'ADAUSDT', 't': 155643455, 'p': '1.86970000', 'q': '108.37000000', 'b': 1468792533, 'a': 1468792553, 'T': 1620964187257, 'm': True, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964187258, 's': 'ADAUSDT', 't': 155643456, 'p': '1.86970000', 'q': '150.00000000', 'b': 1468792541, 'a': 1468792553, 'T': 1620964187257, 'm': True, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964187258, 's': 'ADAUSDT', 't': 155643457, 'p': '1.86950000', 'q': '56.76000000', 'b': 1468792481, 'a': 1468792553, 'T': 1620964187257, 'm': True, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964187258, 's': 'ADAUSDT', 't': 155643458, 'p': '1.86950000', 'q': '237.47000000', 'b': 1468792487, 'a': 1468792553, 'T': 1620964187257, 'm': True, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964187258, 's': 'ADAUSDT', 't': 155643459, 'p': '1.86950000', 'q': '50.00000000', 'b': 1468792487, 'a': 1468792554, 'T': 1620964187258, 'm': True, 'M': True}}
# {'stream': 'adausdt@trade', 'data': {'e': 'trade', 'E': 1620964187823, 's': 'ADAUSDT', 't': 155643460, 'p': '1.86950000', 'q': '3300.00000000', 'b': 1468792603, 'a': 1468792566, 'T': 1620964187821, 'm': False, 'M': True}}
