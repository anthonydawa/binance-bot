import os
from Position import Position
import numpy as np
import talib
from helper_func import get_day_week, get_hour_day, get_key_from_value, return_timeframe_minute
from pattern_indicator import pattern_indicator_backtest
import pickle

class Strategy:
    def __init__(self,risk_ratio,method,timeframe,market,period):
        self.risk_ratio = risk_ratio
        self.method = method
        self.timeframe = timeframe
        self.market = market
        self.period = period
        self.klines = None
        self.position = None
        self.won = False
        self.lost = False
        self.fee = 0.001
        self.delay = 0.002
        self.long_profit = 0
        self.short_profit = 0
        self.long_uptrend_wins = 0
        self.long_downtrend_wins = 0
        self.short_uptrend_wins = 0
        self.short_downtrend_wins = 0
        self.short_losses = 0
        self.short_wins = 0
        self.long_losses = 0
        self.long_wins = 0
    


    def backtest_pattern(self):

        my_save_path = f'historical_klines/{self.market}-klines-{self.period[1]}-{self.timeframe}'
        
        with open(my_save_path,'rb') as f:
            kline_from_file = pickle.load(f)
            
        kline = np.array(kline_from_file)

        d = np.array(kline[:,0],dtype=np.int64)
        o = np.array(kline[:,1],dtype=np.float64)
        h = np.array(kline[:,2],dtype=np.float64)
        l = np.array(kline[:,3],dtype=np.float64)
        c = np.array(kline[:,4],dtype=np.float64)

        EMA = talib.WMA(c,20)
        RSI = talib.RSI(c)
        ATR = talib.ATR(h,l,c)
        CDL = self.method(o,h,l,c)
        


        idx = 20  
        while idx < len(kline) - 1:

            if self.position:

                if l[idx] <= self.position.TP <= h[idx]:
                    self.won = True
                if l[idx] <= self.position.SL <= h[idx]:
                    self.lost = True

                if self.won and self.lost:
                    self.won = False
                    self.lost = False

                elif self.won and not self.lost:

                    gain = 100 * ( (abs(self.position.TP) - abs(self.position.c)) / abs(self.position.c) )
                    gain_with_fee = gain - (gain * (self.fee * 2))
                    gain_with_constant = gain_with_fee - (gain * self.delay) 

                    if self.position.c < self.position.TP:
                        self.long_profit = self.long_profit + gain_with_constant


                        if self.position.Trend == 1:
                            self.long_uptrend_wins = self.long_uptrend_wins + 1
                            self.long_wins = self.long_wins + 1
                        elif self.position.Trend == 0:
                            self.long_downtrend_wins = self.long_downtrend_wins + 1
                            self.long_wins = self.long_wins + 1                       

                    elif self.position.c > self.position.TP:
                        self.short_profit = self.short_profit + gain_with_constant

                        if self.position.Trend == 1:
                            self.short_uptrend_wins = self.short_uptrend_wins + 1
                            self.short_wins = self.short_wins + 1
                        elif self.position.Trend == 0:
                            self.short_downtrend_wins = self.short_downtrend_wins + 1
                            self.short_wins = self.short_wins + 1

                    self.position.trade_result = 1
                    key_of_method = get_key_from_value(pattern_indicator_backtest,self.method)

                    dw = get_day_week(self.position.d)
                    hd = get_hour_day(self.position.d)

                    my_path = f'backtest_data_isolated/{self.market}-{self.period[0]}-{self.period[1]}.csv'
                    #d,o,h,l,c,TP,SL,rr1,rr2,Trend,result,method,dayweek,hourday,timeframe

                    
                    if not os.path.exists(my_path):
                        with open(my_path,'a') as f:
                            f.write(f'd,o,h,l,c,TP,SL,rr1,rr2,trend,rsi,result,method,dw,hd,timeframe\n{self.position.d},{self.position.o},{self.position.h},{self.position.l},{self.position.c},{self.position.TP},{self.position.SL},{self.risk_ratio[0]},{self.risk_ratio[1]},{self.position.Trend},{self.position.rsi},{self.position.trade_result},{key_of_method},{dw},{hd},{return_timeframe_minute(self.timeframe)}\n')                        
                    elif os.path.exists(my_path):
                        with open(my_path,'a') as f:
                            f.write(f'{self.position.d},{self.position.o},{self.position.h},{self.position.l},{self.position.c},{self.position.TP},{self.position.SL},{self.risk_ratio[0]},{self.risk_ratio[1]},{self.position.Trend},{self.position.rsi},{self.position.trade_result},{key_of_method},{dw},{hd},{return_timeframe_minute(self.timeframe)}\n')
                             
                    self.position = None
                    self.won = False
                    self.lost = False


                elif self.lost and not self.won:

                    gain = 100 * ( (abs(self.position.c) - abs(self.position.SL)) / abs(self.position.SL) )
                    gain_with_fee = gain - (gain * (self.fee * 2))
                    gain_with_constant = gain_with_fee - (gain * self.delay) 

                    if self.position.c < self.position.TP:
                        self.long_profit = self.long_profit - gain_with_constant
                        self.long_losses = self.long_losses + 1

                    elif self.position.c > self.position.TP:
                        self.short_profit = self.short_profit - gain_with_constant
                        self.short_losses = self.short_losses + 1
  
                    
                    self.position.trade_result = 0
                    key_of_method = get_key_from_value(pattern_indicator_backtest,self.method)

                    dw = get_day_week(self.position.d)
                    hd = get_hour_day(self.position.d)
                    
                    my_path = f'backtest_data_isolated/{self.market}-{self.period[0]}-{self.period[1]}.csv'

                    if not os.path.exists(my_path):
                        with open(my_path,'a') as f:
                            f.write(f'd,o,h,l,c,TP,SL,rr1,rr2,trend,rsi,result,method,dw,hd,timeframe\n{self.position.d},{self.position.o},{self.position.h},{self.position.l},{self.position.c},{self.position.TP},{self.position.SL},{self.risk_ratio[0]},{self.risk_ratio[1]},{self.position.Trend},{self.position.rsi},{self.position.trade_result},{key_of_method},{dw},{hd},{return_timeframe_minute(self.timeframe)}\n')                        
                    elif os.path.exists(my_path):
                        with open(my_path,'a') as f:
                            f.write(f'{self.position.d},{self.position.o},{self.position.h},{self.position.l},{self.position.c},{self.position.TP},{self.position.SL},{self.risk_ratio[0]},{self.risk_ratio[1]},{self.position.Trend},{self.position.rsi},{self.position.trade_result},{key_of_method},{dw},{hd},{return_timeframe_minute(self.timeframe)}\n')
                    
                    self.position = None
                    self.won = False
                    self.lost = False                    
            
            elif not self.position:

                if CDL[idx] == 100:

                    TP = c[idx] + (self.risk_ratio[0] * ATR[idx])
                    SL = c[idx] - (self.risk_ratio[1] * ATR[idx])

                    if c[idx] < EMA[idx]:
                        TREND = 0
                        self.position = Position(d[idx],o[idx],h[idx],l[idx],c[idx],TP,SL,TREND,RSI[idx])

                    elif c[idx] > EMA[idx]:    
                        TREND = 1
                        self.position = Position(d[idx],o[idx],h[idx],l[idx],c[idx],TP,SL,TREND,RSI[idx])
                    

                elif CDL[idx] == -100:

                    TP = c[idx] - (self.risk_ratio[0] * ATR[idx])   
                    SL = c[idx] + (self.risk_ratio[1] * ATR[idx])

                    if c[idx] < EMA[idx]:
                        TREND = 0
                        self.position = Position(d[idx],o[idx],h[idx],l[idx],c[idx],TP,SL,TREND,RSI[idx])

                    elif c[idx] > EMA[idx]:    
                        TREND = 1
                        self.position = Position(d[idx],o[idx],h[idx],l[idx],c[idx],TP,SL,TREND,RSI[idx])

            idx += 1

        my_save_path2 = f'backtest_data_shared/{self.market}-{self.period[0]}-{self.period[1]}.csv'

        try:
            long_winrate = (self.long_wins / (self.long_losses + self.long_wins)) * 100
        except ZeroDivisionError:
            long_winrate = 0  
        try:
            short_winrate = (self.short_wins / (self.short_losses + self.short_wins)) * 100
        except ZeroDivisionError:
            short_winrate = 0
        try:
            long_uptrend_size = (self.long_uptrend_wins / self.long_wins) * 100 
        except ZeroDivisionError:
            long_uptrend_size = 0
        try:
            long_downtrend_size = (self.long_downtrend_wins / self.long_wins) * 100
        except ZeroDivisionError:
            long_downtrend_size = 0
        try:
            short_uptrend_size = (self.short_uptrend_wins / self.short_wins) * 100
        except ZeroDivisionError:
            short_uptrend_size = 0
        try:
            short_downtrend_size = (self.short_downtrend_wins / self.short_wins) * 100
        except ZeroDivisionError:
            short_downtrend_size = 0

            # market,long_profit,short_profit,losses,wins,uptrend_size,downtrend_size,risk_ratio_0,risk_ratio_1,timeframe,winrate,key_of_method
        try:
            if not os.path.exists(my_save_path2):

                key_of_method = get_key_from_value(pattern_indicator_backtest,self.method)
                with open(my_save_path2,'a') as f:
                    f.write(f'market,long profit,short profit,long wins,short wins,long losses,short losses,long uptrend size,long downtrend size,short uptrend size,short downtrend size,risk ratio tp,risk ratio sl,timeframe,long winrate,short winrate,method,date start,date end\n{self.market},{self.long_profit},{self.short_profit},{self.long_wins},{self.short_wins},{self.long_losses},{self.short_losses},{long_uptrend_size},{long_downtrend_size},{short_uptrend_size},{short_downtrend_size},{self.risk_ratio[0]},{self.risk_ratio[1]},{return_timeframe_minute(self.timeframe)},{long_winrate},{short_winrate},{key_of_method},{self.period[0]},{self.period[1]}\n')               
            
            elif os.path.exists(my_save_path2):

                key_of_method = get_key_from_value(pattern_indicator_backtest,self.method)
                with open(my_save_path2,'a') as f:
                    f.write(f'{self.market},{self.long_profit},{self.short_profit},{self.long_wins},{self.short_wins},{self.long_losses},{self.short_losses},{long_uptrend_size},{long_downtrend_size},{short_uptrend_size},{short_downtrend_size},{self.risk_ratio[0]},{self.risk_ratio[1]},{return_timeframe_minute(self.timeframe)},{long_winrate},{short_winrate},{key_of_method},{self.period[0]},{self.period[1]}\n')

            with open('backtest_checklist/completed_backtest','a') as f:
                f.write(f'{key_of_method},{self.risk_ratio},{self.timeframe},{self.market},{self.period[0]},{self.period[1]}\n')

        except Exception as e:
            print(e)
