from numpy import vander


class Position:
    def __init__(self,d,o,h,l,c,TP,SL,Trend,rsi):
        self.d = d
        self.o = o
        self.h = h
        self.l = l
        self.c = c
        self.TP = TP
        self.SL = SL
        self.Trend = Trend
        self.rsi = rsi
        self.trade_result = None

