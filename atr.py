
from f4 import idx_array
import numpy as np 



def EMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a

def TR(d,h,l,yc):

    x = float(h)-float(l)
    y = abs(float(h)-float(yc))
    z = abs(float(l)-float(yc))
    TR = max(x,y,z)
    return d, TR


def avgtr(candle,window=15):
    date = idx_array(candle,0)
    highp = idx_array(candle,2)
    lowp = idx_array(candle,3)
    closep = idx_array(candle,4)

    x = 1
    TRDates = []
    TrueRanges = []

    while x <len(date):
        TRDate,TrueRange = TR(date[x],highp[x],lowp[x], closep[x-1])
        TRDates.append(TRDate)
        TrueRanges.append(TrueRange)
        x += 1

    ATR = EMovingAverage(TrueRanges,window)

    return ATR





