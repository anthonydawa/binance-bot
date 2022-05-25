from market import init_market
import time
from method_test import Strategy
from helper_func import dict_to_array, get_key_from_value
import os
import pickle
from binance.client import Client
from pattern_indicator import pattern_indicator_backtest

from credentials import apikey, secretkey
client = Client(apikey,secretkey)

class MarketBacktest:
    def __init__(self,risk_ratios,methods,timeframes,markets,periods):
        self.risk_ratios = risk_ratios
        self.methods = methods
        self.timeframes = timeframes
        self.markets = markets
        self.periods = periods
        self.strategies = None

        

    
    def get_klines_from_web(self):

        from os import listdir , remove
        from os.path import isfile, join
        import pickle

        for market in self.markets:
            for timeframe in self.timeframes:

                onlyfiles = [f for f in listdir('historical_klines') if isfile(join('historical_klines', f))]
                targetfiles = [f for f in onlyfiles if market.upper() in f and timeframe in f]

                if targetfiles:
                    tfile = targetfiles[0]

                    with open(f'historical_klines/{tfile}', 'rb' ) as f:
                        previous_data = pickle.load(f)

                    my_save_path = f'historical_klines/{market}-klines-{self.periods[1]}-{timeframe}'
                    
                    if not os.path.exists(my_save_path):
                        if timeframe == '1m':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_1MINUTE,self.periods[0],self.periods[1])
                        elif timeframe == '5m':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_5MINUTE,self.periods[0],self.periods[1])
                        elif timeframe == '15m':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_15MINUTE,self.periods[0],self.periods[1])
                        elif timeframe == '1h':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_1HOUR,self.periods[0],self.periods[1])
                        elif timeframe == '4h':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_4HOUR,self.periods[0],self.periods[1])
                        elif timeframe == '1d':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_1DAY,self.periods[0],self.periods[1])
                        
                        updated_candles = previous_data + candles
                        print('old data exist!')
                        print(market,timeframe)
                        with open(my_save_path ,'wb') as f:
                            pickle.dump(updated_candles,f)  

                        remove(f'historical_klines/{tfile}')

                elif not targetfiles:

                    my_save_path = f'historical_klines/{market}-klines-{self.periods[1]}-{timeframe}'
                    
                    if not os.path.exists(my_save_path):
                        if timeframe == '1m':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_1MINUTE,self.periods[0],self.periods[1])
                        elif timeframe == '5m':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_5MINUTE,self.periods[0],self.periods[1])
                        elif timeframe == '15m':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_15MINUTE,self.periods[0],self.periods[1])
                        elif timeframe == '1h':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_1HOUR,self.periods[0],self.periods[1])
                        elif timeframe == '4h':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_4HOUR,self.periods[0],self.periods[1])
                        elif timeframe == '1d':
                            candles = client.get_historical_klines(market, Client.KLINE_INTERVAL_1DAY,self.periods[0],self.periods[1])

                        print('no old data existing')
                        print(market,timeframe)

                        with open(my_save_path ,'wb') as f:
                            pickle.dump(candles,f)


    def generate_strat(self):

        strats = []

        for method in self.methods:
            for risk_ratio in self.risk_ratios:
                for timeframe in self.timeframes:
                    for market in self.markets:

                        key_of_method = get_key_from_value(pattern_indicator_backtest,method)
                        now_strat = f'{key_of_method},{risk_ratio},{timeframe},{market},{self.periods[0]},{self.periods[1]}'

                        with open('backtest_checklist/completed_backtest','r') as f:

                            lines = f.readlines()
                            format_lines = [x.replace('\n','') for x in lines]

                            if now_strat in format_lines:
                                print('already done', now_strat)
                            elif now_strat not in format_lines:
                                strats.append(Strategy(risk_ratio,method,timeframe,market,self.periods))
                                print('not yet done', now_strat)

        self.strategies = strats

    def run_backtest(self):
        for strats in self.strategies:
            strats.backtest_pattern() 
        print('done all')

methods = dict_to_array(pattern_indicator_backtest)
risk_ratios = [[x/2,y/2] for x in range(2,13) for y in range(2,7) if y < x]
timeframes = ['15m','1h','4h','1d']
markets = [init_market()[14]]
periods = ['5 May 2013','26 June 2021']


x = MarketBacktest(
    risk_ratios=risk_ratios,
    methods=methods,
    timeframes=timeframes,
    markets=markets,
    periods=periods,
    )


if __name__ == "__main__":
    x.get_klines_from_web()
    x.generate_strat()
    x.run_backtest()

# with open('backtest_data_isolated\BTCUSDT-27 May 2021-28 May 2021-5m', 'rb') as f:
#     x = pickle.load(f)
#     print(x)