

from os import X_OK
from talib import stream

from filter_method import return_best_by_timeframe
from kline_initial import klines_initial
import numpy as np

class Candles:

    def __init__(self,symbol,timeframe):
        self.symbol = symbol.upper()
        self.timeframe = timeframe
        self.klines = klines_initial(symbol,timeframe,50)
        self.klines_np = np.array(self.klines)
        self.klines_np_d = self.klines_np[:,0]
        self.klines_np_o = self.klines_np[:,1]
        self.klines_np_h = self.klines_np[:,2]
        self.klines_np_l = self.klines_np[:,3]
        self.klines_np_c = self.klines_np[:,4]
        self.methods = return_best_by_timeframe(symbol,timeframe)
    
    def update(self,new_kline):

        if self.timeframe == '5m':
            datex = int(new_kline['data']['k']['t'])
        elif self.timeframe == '15m':
            datex = self.klines[-1][0] + 900_000
        elif self.timeframe == '1h':
            datex = self.klines[-1][0] + 3_600_000
        elif self.timeframe == '4h':
            datex = self.klines[-1][0] + 14_400_000

        
        openx = float(new_kline['data']['k']['o'])
        highx = float(new_kline['data']['k']['h'])
        lowx = float(new_kline['data']['k']['l'])
        closex = float(new_kline['data']['k']['c'])
        new_kline = [datex,openx,highx,lowx,closex]

        self.klines.remove(self.klines[0])
        self.klines.append(new_kline)
        self.klines_np = np.array(self.klines)
        self.klines_np_d = self.klines_np[:,0]
        self.klines_np_o = self.klines_np[:,1]
        self.klines_np_h = self.klines_np[:,2]
        self.klines_np_l = self.klines_np[:,3]
        self.klines_np_c = self.klines_np[:,4]

        ATR = stream.ATR(self.klines_np_h,self.klines_np_l,self.klines_np_c)


        x = []

        for m in self.methods:

            mt = m[0](self.klines_np_o,self.klines_np_h,self.klines_np_l,self.klines_np_c)

            if mt == 100:

                TP = closex + (( float(m[1])) * (ATR))
                SL = closex - (( float(m[2])) * (ATR))

                order = [TP,SL]

                x.append(order)

        return x 



    

# c = Candles('adausdt','5m')
# print(c.methods)



