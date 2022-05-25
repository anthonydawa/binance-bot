import datetime
from market import init_market
import os
import talib
import pickle
import numpy as np
from binance.client import Client
from binance.enums import *
from credentials import apikey, secretkey

client = Client(apikey,secretkey)

tickers = client.get_ticker()
USDT_PAIRS = []
for t in tickers:
    if 'USDT' in t['symbol']:
        USDT_PAIRS.append(t['symbol'])


#NEOBNBONT
PERIOD = ['6 May 2021','12 May 2021']
RISK_REWARDS = [[2,2],[2.5,2],[2,1],[1.5,1],[3,2],[5,3],[4,1],[3,1],[4,2],[3.5,2],[5,1],[6,1],[5,2],[6,2],[6,3],[1,1],[1.3,1],[5,2]]

MARKETS = init_market()
TIMEFRAMES = ['5m','15m','1h','4h']

def candle_difference(o,c):
    increase = c - o
    percent_diff = increase / o * 100
    return percent_diff 

def klines_initial(symbol,period,range_start,range_end,kline_to_store):
    print(symbol)
    rsx = range_start.replace(" ","").replace(",","")
    rex = range_end.replace(" ","").replace(",","")

    my_path = f'HISTORICAL_DATA/{symbol}-klines-{rsx}-{rex}-{period}'
    
    if os.path.exists(my_path):
        with open(my_path,'rb') as f:
            data = pickle.load(f)
        # my_data = np.genfromtxt(my_path, delimiter=',')
        # print(my_data)
            print('from file')
            kline_to_store.append(np.array(data))

    else:
        if period == '1m':
            candles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE,range_start,range_end)
        elif period == '5m':
            candles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE,range_start,range_end)
        elif period == '15m':
            candles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE,range_start,range_end)
        elif period == '1h':
            candles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1HOUR,range_start,range_end)
        elif period == '4h':
            candles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_4HOUR,range_start,range_end)
        elif period == '1d':
            candles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY,range_start,range_end)

        candle_array = []

        if candles:
            for candle in candles:
                d = int(candle[0])
                o = float(candle[1])
                h = float(candle[2])
                l = float(candle[3])
                c = float(candle[4])
                kline = [d,o,h,l,c]
                candle_array.append(kline)

            # with open(my_path ,'w') as f:
            #     f.write(f'{d},{o},{h},{l},{c},')
            with open(my_path ,'wb') as f:
                pickle.dump(candle_array,f)

            print('from web')
            kline_to_store.append(np.array(candle_array)) 

def multiple_backtest(market_arr,timeframe_arr,risk_arr,range_start,range_end):
    #will have an array of np arr 
    KLINES = []

    for mrk in market_arr:
        for tf in timeframe_arr:
            klines_initial(mrk,tf,range_start,range_end,KLINES)

    if KLINES:
        idx_arr = []
        countxx = []
        countyy = []
        countx = 0
        county = 0

        for _ in market_arr:
            countxx.append(countx)
            countx += 1
        for _ in timeframe_arr:
            countyy.append(county)
            county +=1

        for x in countxx:
            for y in countyy:
                idx_arr.append([x,y])

        count = 0
        for kls in KLINES:
            d = np.array(kls[:,0],dtype=np.int64)
            o = np.array(kls[:,1],dtype=np.float64)
            h = np.array(kls[:,2],dtype=np.float64)
            l = np.array(kls[:,3],dtype=np.float64)
            c = np.array(kls[:,4],dtype=np.float64)

            EMA50 = talib.WMA(c,50)
            RSI = talib.RSI(c,14)
            ATR = talib.ATR(h,l,c)
            computed_methods = compute_methods(o,h,l,c)
            market_arrx = market_arr[idx_arr[count][0]]
            timeframe_arrx = timeframe_arr[idx_arr[count][1]]
            TEST_ALL(computed_methods,d,o,h,l,c,EMA50,RSI,ATR,risk_arr,market_arrx,timeframe_arrx)
            
            count += 1


def compute_methods(o,h,l,c):

    ALL_METHODS = []
    ALL_METHODS.append(talib.CDL2CROWS(o,h,l,c))
    ALL_METHODS.append(talib.CDL3BLACKCROWS(o,h,l,c))
    ALL_METHODS.append(talib.CDL3INSIDE(o,h,l,c))
    ALL_METHODS.append(talib.CDL3LINESTRIKE(o,h,l,c))
    ALL_METHODS.append(talib.CDL3OUTSIDE(o,h,l,c))
    ALL_METHODS.append(talib.CDL3STARSINSOUTH(o,h,l,c))
    ALL_METHODS.append(talib.CDL3LINESTRIKE(o,h,l,c))
    ALL_METHODS.append(talib.CDL3WHITESOLDIERS(o,h,l,c))
    ALL_METHODS.append(talib.CDLABANDONEDBABY(o,h,l,c))
    ALL_METHODS.append(talib.CDLADVANCEBLOCK(o,h,l,c))
    ALL_METHODS.append(talib.CDLBELTHOLD(o,h,l,c))
    ALL_METHODS.append(talib.CDLBREAKAWAY(o,h,l,c))
    ALL_METHODS.append(talib.CDLCLOSINGMARUBOZU(o,h,l,c))
    ALL_METHODS.append(talib.CDLCONCEALBABYSWALL(o,h,l,c))
    ALL_METHODS.append(talib.CDLCOUNTERATTACK(o,h,l,c))
    ALL_METHODS.append(talib.CDLDARKCLOUDCOVER(o,h,l,c))
    ALL_METHODS.append(talib.CDLDOJI(o,h,l,c))
    ALL_METHODS.append(talib.CDLDOJISTAR(o,h,l,c))
    ALL_METHODS.append(talib.CDLDRAGONFLYDOJI(o,h,l,c))
    ALL_METHODS.append(talib.CDLENGULFING(o,h,l,c))
    ALL_METHODS.append(talib.CDLEVENINGDOJISTAR(o,h,l,c))
    ALL_METHODS.append(talib.CDLEVENINGSTAR(o,h,l,c))
    ALL_METHODS.append(talib.CDLGAPSIDESIDEWHITE(o,h,l,c))
    ALL_METHODS.append(talib.CDLGRAVESTONEDOJI(o,h,l,c))
    ALL_METHODS.append(talib.CDLHAMMER(o,h,l,c))
    ALL_METHODS.append(talib.CDLHANGINGMAN(o,h,l,c))
    ALL_METHODS.append(talib.CDLHARAMI(o,h,l,c))
    ALL_METHODS.append(talib.CDLHARAMICROSS(o,h,l,c))
    ALL_METHODS.append(talib.CDLHIGHWAVE(o,h,l,c))
    ALL_METHODS.append(talib.CDLHIKKAKE(o,h,l,c))
    ALL_METHODS.append(talib.CDLHIKKAKEMOD(o,h,l,c))
    ALL_METHODS.append(talib.CDLHOMINGPIGEON(o,h,l,c))
    ALL_METHODS.append(talib.CDLIDENTICAL3CROWS(o,h,l,c))
    ALL_METHODS.append(talib.CDLINNECK(o,h,l,c))
    ALL_METHODS.append(talib.CDLINVERTEDHAMMER(o,h,l,c))
    ALL_METHODS.append(talib.CDLKICKING(o,h,l,c))
    ALL_METHODS.append(talib.CDLKICKINGBYLENGTH(o,h,l,c))
    ALL_METHODS.append(talib.CDLLADDERBOTTOM(o,h,l,c))
    ALL_METHODS.append(talib.CDLLONGLEGGEDDOJI(o,h,l,c))
    ALL_METHODS.append(talib.CDLLONGLINE(o,h,l,c))
    ALL_METHODS.append(talib.CDLMARUBOZU(o,h,l,c))
    ALL_METHODS.append(talib.CDLMATCHINGLOW(o,h,l,c))
    ALL_METHODS.append(talib.CDLMATHOLD(o,h,l,c))
    ALL_METHODS.append(talib.CDLMORNINGDOJISTAR(o,h,l,c))
    ALL_METHODS.append(talib.CDLMORNINGSTAR(o,h,l,c))
    ALL_METHODS.append(talib.CDLONNECK(o,h,l,c))
    ALL_METHODS.append(talib.CDLPIERCING(o,h,l,c))
    ALL_METHODS.append(talib.CDLRICKSHAWMAN(o,h,l,c))
    ALL_METHODS.append(talib.CDLRISEFALL3METHODS(o,h,l,c))
    ALL_METHODS.append(talib.CDLSEPARATINGLINES(o,h,l,c))
    ALL_METHODS.append(talib.CDLSHOOTINGSTAR(o,h,l,c))
    ALL_METHODS.append(talib.CDLSHORTLINE(o,h,l,c))
    ALL_METHODS.append(talib.CDLSPINNINGTOP(o,h,l,c))
    ALL_METHODS.append(talib.CDLSTALLEDPATTERN(o,h,l,c))
    ALL_METHODS.append(talib.CDLSTICKSANDWICH(o,h,l,c))
    ALL_METHODS.append(talib.CDLTAKURI(o,h,l,c))
    ALL_METHODS.append(talib.CDLTASUKIGAP(o,h,l,c))
    ALL_METHODS.append(talib.CDLTHRUSTING(o,h,l,c))
    ALL_METHODS.append(talib.CDLTRISTAR(o,h,l,c))
    ALL_METHODS.append(talib.CDLUNIQUE3RIVER(o,h,l,c))
    ALL_METHODS.append(talib.CDLUPSIDEGAP2CROWS(o,h,l,c))
    ALL_METHODS.append(talib.CDLXSIDEGAP3METHODS(o,h,l,c))
    return ALL_METHODS




def TEST_ALL(method_array,d,o,h,l,c,EMA50,RSI,ATR,RR,SYMBOL,tfr):
    count_method = []
    for method in method_array:
        count_method.append(0)
        for rrs in RR:
            backtesting_strategy(d,o,h,l,c,EMA50,RSI,ATR,method,SYMBOL,len(count_method),rrs,tfr)
            

def backtesting_strategy(d,o,h,l,c,ema50,rsi,atr,method,symbol,count_method,riskreward,tfr):

    counter = []
    take_profit = []
    stop_loss = []

    PROFIT = []
    NA = []
    LOSS = []

    count = 0
    completed = False

    while not completed:
        if count < len(o)-1:
            if np.isnan(ema50[count]) == False:
                
                dayx = d[count]
                openx = o[count]
                highx = h[count]
                lowx = l[count]
                closex = c[count]
                emax = ema50[count]
                rsix = rsi[count]
                atrx = atr[count]
                methodx = method[count]

                if take_profit and stop_loss:

                    TPF = False
                    SLF = False

                    if lowx <= take_profit[0] <= highx:
                        TPF = True
                    if lowx <= stop_loss[0] <= highx:
                        SLF = True

                    if TPF and SLF:
                        NA.append(True)   
                        # t = int(dayx)
                        # timestamp = str(t)
                        # your_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)
                        # with open(f'WINRATES-{symbol}', 'a') as f:
                        #     f.write(f'{your_dt},{take_profit[0]},{stop_loss[0]},NA\n')
                        take_profit.pop()
                        stop_loss.pop()  

                    elif TPF and not SLF:
                        PROFIT.append(True)
                        # print('WIN',symbol)
                        # t = int(dayx)
                        # timestamp = str(t)
                        # your_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)
                        with open(f'WINRATES-{symbol}', 'a') as f:
                            f.write(f'{dayx},{openx},{highx},{lowx},{closex},{emax},{atrx},{rsix},{methodx},{take_profit[0]},{stop_loss[0]},True\n')
                        take_profit.pop()
                        stop_loss.pop()

                    elif not TPF and SLF:
                        LOSS.append(True)
                        # print('LOSS',symbol)
                        # t = int(dayx)
                        # timestamp = str(t)
                        # your_dt = datetime.datetime.fromtimestamp(int(timestamp)/1000)
                        with open(f'WINRATES-{symbol}', 'a') as f:
                            f.write(f'{dayx},{openx},{highx},{lowx},{closex},{emax},{atrx},{rsix},{methodx},{take_profit[0]},{stop_loss[0]},False\n')    
                        take_profit.pop()
                        stop_loss.pop()   

                    elif not TPF and not SLF:
                        pass


                elif not take_profit and not stop_loss:

                    if methodx == 100 :
                        TP = closex + (riskreward[0]) * (atrx)
                        SL = closex - (riskreward[1]) * (atrx)
                        take_profit.append(TP)
                        stop_loss.append(SL)                 

                count += 1

                # with open(f'DATAS-{symbol}', 'a') as f:
                #     f.write(f'{dayx},{openx},{highx},{lowx},{closex},{emax},{atrx},{rsix},{methodx}\n')

            elif np.isnan(ema50[count]) == True:
                count += 1
        elif count == len(o)-1:
            total = len(PROFIT) + len(LOSS)
            path_to_file = f'c:/Users/tiamat/Desktop/tiamat/result/{symbol}-{PERIOD[0]}-{PERIOD[1]}-RESULTS.csv'
            if total:
                winrate = (len(PROFIT) / total) * (100)
                gains = ( ( (len(PROFIT) * riskreward[0]) - (len(LOSS) * riskreward[1]) ) * (timeframe_mult(tfr)) )
                
                with open(path_to_file, 'a') as f:
                    f.write(f'{winrate},{len(PROFIT)},{len(LOSS)},{total},{riskreward[0]},{riskreward[1]},{tfr},{PERIOD[0]},{PERIOD[1]},{symbol},{count_method},{gains}\n')
            if not total:
                with open(path_to_file, 'a') as f:
                    f.write(f'{0},{0},{0},{0},{riskreward[0]},{riskreward[1]},{tfr},{PERIOD[0]},{PERIOD[1]},{symbol},{count_method},0\n')
            completed = True

def timeframe_mult(TIMEFRAME):
    if TIMEFRAME == '1m':
        return 0.5
    elif TIMEFRAME == '5m':
        return 1
    elif TIMEFRAME == '15m':
        return 2
    elif TIMEFRAME == '1h':
        return 4
    elif TIMEFRAME == '4h':
        return 7
    elif TIMEFRAME == '1d':
        return 8   

multiple_backtest(MARKETS,TIMEFRAMES,RISK_REWARDS,PERIOD[0],PERIOD[1])