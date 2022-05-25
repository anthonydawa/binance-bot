import pickle
import time
from kline_initial import klines_initial
from filter_method import return_best_methods
from binance.client import Client
from binance.enums import *
from credentials import apikey, secretkey

client = Client(apikey,secretkey)


def finalized ():


    
    tickers = client.get_ticker()

    x = ['USDSBUSDT','USDTBKRW','USDTGYEN','SUSDUSDT','BCHABCUSDT','BCHSVUSDT','SHIBAUSDT','BCCUSDT','USDCUSDT','TUSDUSDT','DOGEUSDT','USDTUAH','USDTIDRT','EURUSDT','USDTRUB','USDTTRY','BUSDTRY','BUSDUSDT','USDTBIDR','USDSUSDT','USDTBRL','USDTZAR','USDTNGN','USDTBVND','USDTDAI']   

    

    USDT_PAIRS = []
    for t in tickers:
        if 'USDT' in t['symbol']:
            if not 'BEAR' in t['symbol']:
                if not 'BULL' in t['symbol']:
                    if not t['symbol'] in x:
                        if not 'DOWN' in t['symbol']:
                            if not 'UP' in t['symbol']:
                                USDT_PAIRS.append(t['symbol'])
    
    

    remove_unqualified = []
    
    for market in USDT_PAIRS:
        result,symbol = return_best_methods(market)
        # print(market)
        # print(result)
        if not result:
            remove_unqualified.append(symbol)
    
    final = []

    for market in USDT_PAIRS:
        if not market in remove_unqualified:
            final.append(market)

    super_final = []  

    for f in final:
        try:
            x = klines_initial(f,'5m',50)
            super_final.append(f)
            print(f)
            time.sleep(0.1)
        except:
            pass

    return super_final


def set_cached_market(arr):
    with open('cached_market.pickle','wb') as f:
        pickle.dump(arr,f)

def get_cached_market():
    with open('cached_market.pickle','rb') as f:
        data = pickle.load(f)
        return data




def init_market():
    x = ['USDSBUSDT','USDTBKRW','USDTGYEN','SUSDUSDT','BCHABCUSDT','BCHSVUSDT','SHIBAUSDT','BCCUSDT','USDCUSDT','TUSDUSDT','DOGEUSDT','USDTUAH','USDTIDRT','EURUSDT','USDTRUB','USDTTRY','BUSDTRY','BUSDUSDT','USDTBIDR','USDSUSDT','USDTBRL','USDTZAR','USDTNGN','USDTBVND','USDTDAI']   


    tickers = client.get_ticker()
    USDT_PAIRS = []
    for t in tickers:
        if 'USDT' in t['symbol']:
            if not 'BEAR' in t['symbol']:
                if not 'BULL' in t['symbol']:
                    if not t['symbol'] in x:
                        if not 'DOWN' in t['symbol']:
                            if not 'UP' in t['symbol']:
                                USDT_PAIRS.append(t['symbol'])
    return USDT_PAIRS


if __name__ == '__main__':
    print(init_market()[0])

# def unqualifed():
#     remove_unqualified = []
#     for market in selected_market():
#         result,symbol = return_best_methods(market)
#         if not result:
#             remove_unqualified.append(symbol)
#     return remove_unqualified

# # print(unqualifed())

# # print(selected_market())

# def qualified_markets():
#     final = []
#     for markets in selected_market():
#         if not selected_market() in unqualifed():
#             final.append(markets)
#     return final

