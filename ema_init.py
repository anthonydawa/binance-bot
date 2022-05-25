from ema import ExpMovingAverage
from get_kline_history import get_200_closed, get_200_latest_klines, klines_init
import pickle
import numpy as np

arp = ['ETHUSDT','ADAUSDT','BTCUSDT','BNBUSDT']

# def ema_init(pairs):
#     klines_init(pairs)
#     klines = get_200_latest_klines(pairs)
#     closed_klines = get_200_closed(klines)
#     emaas = []
#     for closed_kline in closed_klines:
#         last_ema = []
#         ema_to_file = []
#         e12 = ExpMovingAverage(closed_kline,12)
#         e25 = ExpMovingAverage(closed_kline,25)
#         e50 = ExpMovingAverage(closed_kline,50)
#         e200 = ExpMovingAverage(closed_kline,200)
#         # for pp in arp:
#         #     with open('EE', 'wb') as file:
#         #         pickle.dump(ema_to_file,file)
#         last_ema.append([e12[len(e12)-1],e25[len(e25)-1],e50[len(e50)-1],e200[len(e200)-1]])
#         emaas.append(last_ema)
#     print(emaas)

def ema_init(closed,window):
    x = []
    for c in closed:
        x.append(ExpMovingAverage(c,window))
    return np.array(x)
