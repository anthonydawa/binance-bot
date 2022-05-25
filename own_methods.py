


import talib

def OVERBOUGHT(o,h,l,c):
    rsi = talib.RSI(c,10)
    y = []
    for x in rsi:
        if x >= 70 :
            y.append(100)
        elif x < 70:
            y.append(0)
        elif x <= 30:
            y.append(-100)
    return y