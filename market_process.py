


import numpy as np
from binance.client import Client
from binance.enums import *
from credentials import apikey, secretkey
import time

from pattern_indicator import pattern_indicator
from filter_method import return_best_methods
from market_order import count_decimal
from kline_initial import klines_initial

client = Client(apikey,secretkey)

def market_process(symbol,kline):
# create kline init for these
    print(symbol,'initialized..')


    patterns = pattern_indicator
    symbol = str(symbol).upper()

    kline_5m = klines_initial(symbol,'5m',50)
    kline_15m = klines_initial(symbol,'15m',50)
    kline_1h = klines_initial(symbol,'1h',50)
    kline_4h = klines_initial(symbol,'4h',50)

    kline_5m_arr = [np.array(kline_5m)]
    kline_5m_np = [kline_5m_arr[0]]
    kline_5m_d = [kline_5m_np[0][:,0]]
    kline_5m_o = [kline_5m_np[0][:,1]]
    kline_5m_h = [kline_5m_np[0][:,2]]
    kline_5m_l = [kline_5m_np[0][:,3]]
    kline_5m_c = [kline_5m_np[0][:,4]]
    
    kline_15m_arr = [np.array(kline_15m)]
    kline_15m_np = [kline_15m_arr[0]]
    kline_15m_d = [kline_15m_np[0][:,0]]
    kline_15m_o = [kline_15m_np[0][:,1]]
    kline_15m_h = [kline_15m_np[0][:,2]]
    kline_15m_l = [kline_15m_np[0][:,3]]
    kline_15m_c = [kline_15m_np[0][:,4]]

    kline_1h_arr = [np.array(kline_1h)]
    kline_1h_np = [kline_1h_arr[0]]
    kline_1h_d = [kline_1h_np[0][:,0]]
    kline_1h_o = [kline_1h_np[0][:,1]]
    kline_1h_h = [kline_1h_np[0][:,2]]
    kline_1h_l = [kline_1h_np[0][:,3]]
    kline_1h_c = [kline_1h_np[0][:,4]]

    kline_4h_arr = [np.array(kline_4h)]
    kline_4h_np = [kline_4h_arr[0]]
    kline_4h_d = [kline_4h_np[0][:,0]]
    kline_4h_o = [kline_4h_np[0][:,1]]
    kline_4h_h = [kline_4h_np[0][:,2]]
    kline_4h_l = [kline_4h_np[0][:,3]]
    kline_4h_c = [kline_4h_np[0][:,4]]

    methods_5m = []
    methods_15m = []
    methods_1h = []
    methods_4h = []


    details = client.get_symbol_info(str(symbol).upper())
    lot_size = count_decimal(details['filters'][0]['tickSize'])
    price_filter = count_decimal(details['filters'][2]['stepSize'])

# sample    
# ['42.19178082191781', '462', '633', '1095', '3', '2', '5m', '1 Jan 2021', '28 April 2021', 'ADAUSDT', '17', '120\n']
    best_methods, _ = return_best_methods(symbol)

    for arr in best_methods:
        timeframe = arr[6]
        method_num = patterns[int(arr[-2])]
        risk_win = arr[4]
        risk_loss = arr[5]
        formatx = [method_num,risk_win,risk_loss]

        if timeframe == '5m':
            methods_5m.append(formatx)
        elif timeframe == '15m':
            methods_15m.append(formatx)
        elif timeframe == '1h':
            methods_1h.append(formatx)
        elif timeframe == '4h':
            methods_4h.append(formatx)
            

    while True:
        print('working',symbol)
        if kline:
            # print(symbol,kline)
            popped_kline = kline.pop()
            datex = int(popped_kline['data']['E'])
            openx = float(popped_kline['data']['k']['o'])
            highx = float(popped_kline['data']['k']['h'])
            lowx = float(popped_kline['data']['k']['l'])
            closex = float(popped_kline['data']['k']['c'])
            timeframex = str(popped_kline['data']['k']['i'])
            new_kline = [datex,openx,highx,lowx,closex]
            
            

            if timeframex == '5m':
                
                kline_5m.remove(kline_5m[0])
                kline_5m.append(new_kline)
                kline_5m_arr.pop()
                kline_5m_arr.append(np.array(kline_5m))
                kline_5m_np.pop()
                kline_5m_np.append(kline_5m_arr[0])
                kline_5m_d.pop()
                kline_5m_d.append(kline_5m_np[0][:,0])
                kline_5m_o.pop()
                kline_5m_o.append(kline_5m_np[0][:,1])
                kline_5m_h.pop()
                kline_5m_h.append(kline_5m_np[0][:,2])
                kline_5m_l.pop()
                kline_5m_l.append(kline_5m_np[0][:,3])
                kline_5m_c.pop()
                kline_5m_c.append(kline_5m_np[0][:,4])
                
            #apply indicator here

                # for method in methods_5m:
                #     my_method = method[0](kline_5m_o,kline_5m_h,kline_5m_l,kline_5m_c)
                #     if my_method[-1] == 100:
                #         print('its a buy')
                        

            elif timeframex == '15m':

                kline_15m.remove(kline_15m[0])
                kline_15m.append(new_kline)
                kline_15m_arr.pop()
                kline_15m_arr.append(np.array(kline_15m))
                kline_15m_np.pop()
                kline_15m_np.append(kline_15m_arr[0])
                kline_15m_d.pop()
                kline_15m_d.append(kline_15m_np[0][:,0])
                kline_15m_o.pop()
                kline_15m_o.append(kline_15m_np[0][:,1])
                kline_15m_h.pop()
                kline_15m_h.append(kline_15m_np[0][:,2])
                kline_15m_l.pop()
                kline_15m_l.append(kline_15m_np[0][:,3])
                kline_15m_c.pop()
                kline_15m_c.append(kline_15m_np[0][:,4])

            elif timeframex == '1h':

   
                kline_1h.remove(kline_1h[0])
                kline_1h.append(new_kline)
                kline_1h_arr.pop()
                kline_1h_arr.append(np.array(kline_1h))
                kline_1h_np.pop()
                kline_1h_np.append(kline_1h_arr[0])
                kline_1h_d.pop()
                kline_1h_d.append(kline_1h_np[0][:,0])
                kline_1h_o.pop()
                kline_1h_o.append(kline_1h_np[0][:,1])
                kline_1h_h.pop()
                kline_1h_h.append(kline_1h_np[0][:,2])
                kline_1h_l.pop()
                kline_1h_l.append(kline_1h_np[0][:,3])
                kline_1h_c.pop()
                kline_1h_c.append(kline_1h_np[0][:,4])


            elif timeframex == '4h':


                kline_4h.remove(kline_4h[0])
                kline_4h.append(new_kline)
                kline_4h_arr.pop()
                kline_4h_arr.append(np.array(kline_4h))
                kline_4h_np.pop()
                kline_4h_np.append(kline_4h_arr[0])
                kline_4h_d.pop()
                kline_4h_d.append(kline_4h_np[0][:,0])
                kline_4h_o.pop()
                kline_4h_o.append(kline_4h_np[0][:,1])
                kline_4h_h.pop()
                kline_4h_h.append(kline_4h_np[0][:,2])
                kline_4h_l.pop()
                kline_4h_l.append(kline_4h_np[0][:,3])
                kline_4h_c.pop()
                kline_4h_c.append(kline_4h_np[0][:,4])     
                    
        time.sleep(1)


