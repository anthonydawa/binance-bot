





def hammer_strategy(o,h,l,c,atr,ema50,bullish,counter,market,symbol,stop_loss,take_profit,STOP_LOSS_ARRAY,PRICE_LIMIT_DECIMAL,COIN_DECIMAL):
    if not counter:
        if c < ema50:
            difference = h - l
            limit_amt = difference * 0.3
            limit_value = h + limit_amt
            min_value = min(c,o)
            if min_value < limit_value:
                print('hammer candle waiting for green candle')
                counter.append(True)
    elif counter:
        if bullish > 0 and c < ema50:
            tp = z + (1.8) * (xatr)
            slp = z - (1.2) * (xatr)
            buy_market_order(mrkt,sl,slp,loss_streak,dec=deci)
            sell_limit_order(tp,symbol,mrkt,order,sl,price_limit_dec,dec=deci)            

