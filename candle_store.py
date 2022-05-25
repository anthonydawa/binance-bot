candle_closed = [] 
candle_open = []

def store_candle(candle, status):
    if status == False:
        candle_open.append(candle)
    else:
        candle_closed.append(candle)

def get_candle(status):
    if status == True:
        return candle_closed
    else:
        return candle_open


