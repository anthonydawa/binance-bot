from binance.client import Client

from binance.enums import *

import numpy as np

apikey = 'ANAETF54sYFzwTWaSLwJQgxzwDsPZabEQyOxRPavibhuHd8Xr8yI82qxeUZffYbz'
secretkey = '7pjB1jjy1nJiuxlhxbcf263sb4Ug3Qz486CfdtFqG2WPznfvduNOCa1X6zSfBCXQ'

client = Client(apikey,secretkey)

max_trade_amt = 0.999
dec_price = 5
price_change_min = 0.1

def upper_case (array):
    x = []
    for arr in array:
        x.append(arr.upper())
    return x

def initial_klines(symbols,days=1):
    for symbol in symbols:
        klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, f"{days} day ago UTC")
        last_200 = klines[-210:]
        kls = []
        for x in last_200:
            d = int(x[0])
            o = float(x[1])
            h = float(x[2])
            l = float(x[3])
            c = float(x[4])
            kl = [d,o,h,l,c]
            kls.append(kl)
        kls.remove(kls[len(kls)-1])
        return kls

        # return last_200

def ExpMa(values,window):
    # vals=[]
    # for x in values:
    #     convert_to_int = float(x)
    #     # rounded = round(convert_to_int,4)
    #     vals.append(convert_to_int)
    weights = np.exp(np.linspace(-1.,0.,window))
    weights /= weights.sum()

    a = np.convolve(values,weights,mode='full') [:len(values)]
    a[:window] = a[window]
    return a


def watch_data(bf,ltkl,ltc,lt200,lt50,at15,rs14,bl):
    if bf:
        x = bf[len(bf)-1]
        datex = int(x['data']['E'])
        openx = float(x['data']['k']['o'])
        highx = float(x['data']['k']['h'])
        lowx = float(x['data']['k']['l'])
        closex = float(x['data']['k']['c'])
        kline = [datex,openx,highx,lowx,closex]
        # if kline[4] == ltkl[len(ltkl)-1][4]:
        #     print('same')
        #     print(kline[4],ltkl[len(ltkl)-1])
        # else:
        ltkl.remove(ltkl[0])
        ltkl.append(kline)
        ltc.remove(ltc[0])
        ltc.append(kline[4])
        x1 = ExpMa(ltc,200)
        x2 = ExpMa(ltc,50)
        x3 = AverageTrueRange(ltkl)
        x4 = RelativeStrengthIndex(ltc)
        x5 = candle_read(openx,closex)
        # if len(lt200) >= 3:
        #     lt200.pop()
        #     lt50.pop()
        #     at15.pop()
        #     lt200.append(x1[len(x1)-1])
        #     lt50.append(x2[len(x2)-1])
        #     at15.append(x3[len(x3)-1])
        # else:
        lt200.append(x1[len(x1)-1])
        lt50.append(x2[len(x2)-1])
        at15.append(x3[len(x3)-1])
        rs14.append(x4[len(x4)-1])
        bl.append(x5)

            
            
def idx_array(arr,idx):
    new_arr = []
    for a in arr:
        new_arr.append(a[idx])
    return new_arr


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


def AverageTrueRange(candle,window=12):
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


def RelativeStrengthIndex(prices, n=14):
 
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n,len(prices)):
        delta = deltas[i-1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1)+upval)/n
        down = (down*(n-1)+downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi

def watch_closed(m200,m50,a15,r15,bf,ct,rt,sl,bls,mrkt,symbol,deci,order):

    if bf and m200 and m50 and a15 and r15 and bls:
        x = bf.pop()
        dayx = x['data']['E']
        y = x['data']['k']['c']
        opx = x['data']['k']['o']
        z = float(y)
        zx = float(opx)
        x50 = m50.pop()
        x200 = m200.pop()
        xatr = a15.pop()
        xrsi = r15.pop()
        print('---------------------------')
        print('|200 EMA:',x200,'|50 EMA:', x50, '|RSI :', xrsi , '|ATR :' ,xatr ,'|PRICE:',z , '|')



        # if xrsi < 22:
        #     rsi_tp = z + (1.5) * (xatr + xatr)
        #     rsi_sl = z - xatr
        #     print('rsi is below 22:', xrsi)
        #     buy_market_order(mrkt,sl,rsi_sl,dec=deci)
        #     sell_limit_order(rsi_tp,symbol,mrkt,order,sl,dec=deci)
        #     with open('engulfing-trades', 'a') as fs:
        #         fs.write(f'{dayx},{x50},{x200},{xatr},{xrsi},{z},{zx},{rsi_tp}\n')



        if len(bls) == 4:
            bls.remove(bls[0])
        if len(bls) == 3:
            if x200 < z:
                candle_oldest = bls[0]
                candle_prev = bls[1]
                candle_now = bls[2]
                if candle_oldest < 0 and candle_prev < 0 and candle_now > 0 and abs(candle_prev) < candle_now :
                    print('bullish engulfing!','CANDLE 3:',candle_oldest, 'PREVIOUS CANDLE:', candle_prev,'CURRENT CANDLE:', candle_now)
                    if abs(candle_prev) <= 0.02 and candle_now <= price_change_min :
                        print('will not buy candle too short!',candle_now)
                    elif candle_now > price_change_min and xrsi < 65 and xrsi > 30:
                        if not sl:
                            print('percent change is 1 percent LOWER')
                            chnge = z-zx
                            prft = chnge
                            # tp = z + prft
                            tp = z + (2) * (xatr)
                            slp = z - xatr
                            print('take profit change : ',chnge, 'profit amount', prft, 'tp:',tp, 'percent change:',candle_now)
                            buy_market_order(mrkt,sl,slp,dec=deci)
                            sell_limit_order(tp,symbol,mrkt,order,sl,dec=deci)
                            print('its a buy',candle_now,'tp:',tp)
                            with open('engulfing-trades', 'a') as fs:
                                fs.write(f'{dayx},{x50},{x200},{xatr},{xrsi},{z},{zx},{tp},{candle_prev}\n') 
                        # elif not sl and candle_now > 0.28 and candle_now < 1.25 and xrsi < 45:
                        #     print('percent change is 1 percent HIGHER')
                        #     chnge = z-zx
                        #     prft = chnge
                        #     # tp = z + prft
                        #     tp = z + (1.5) * (xatr + xatr)
                        #     slp = z - xatr
                        #     print('take profit change : ',chnge, 'tp:',tp, 'percent change:',candle_now)
                        #     buy_market_order(mrkt,sl,slp,dec=deci)
                        #     sell_limit_order(tp,symbol,mrkt,order,sl,dec=deci)
                        #     print('its a buy',candle_now,'tp:',tp)
                        #     with open('engulfing-trades', 'a') as fs:
                        #         fs.write(f'{dayx},{x50},{x200},{xatr},{xrsi},{z},{zx},{tp}\n')
                        elif not sl and xrsi > 65:
                            print('not buying candle rsi is overbought', xrsi)



                    elif xrsi < 45 or xrsi > 65:
                        print('rsi is below 50 or above 85', xrsi)
                    else:
                        print('did not buy candle too short')
                else:
                    print('NOT bullish engulfing!', 'candle 1:', candle_prev,'candle 2:', candle_now)
            elif x200 > z:
                print('price is below 200 ema',z,x200)


        if not ct:
            if x50 < x200:
                print(x50, '50 ema is lower than 200', x200, '@', len(ct))
                ct.append(True)
            elif x50> x200:
                print( x50, '50 ema is higher than 200', x200, '@',len(ct))
        elif len(ct) == 1:
            if x50 > x200 and z > x50:
                print( x50, '50 ema is higher than 200', x200, '@',len(ct))
                ct.append(True)
            elif x50 < x200:
                print( x50, '50 ema is lower than 200', x200, '@',len(ct))
        elif len(ct) == 2:
            if z < x50:
                ct.append(True)
                print(z,'price has dipped below 50ma waiting for re entry',x50 ,'@',len(ct))
            elif z > x50:
                print( z, 'price is still above 50ma waiting for 1st dip below...',x50,'@',len(ct))
        elif len(ct) == 3:
            if len(rt) == 4:
                print('retries more than 3 :', len(rt))
                rt.clear()
                ct.clear()
            elif len(rt) < 4:
                if z > x50:
                    print(z, 'price pullback to 50ma buy signal', x50, '@',len(ct))
                    sls = z - xatr - xatr
                    pts = z + (1.5) * (xatr + xatr)
                    buy_market_order(mrkt,sl,sls,dec=deci)
                    sell_limit_order(pts,symbol,mrkt,order,dec=deci)
                    with open('engulfing-trades', 'a') as fs:
                        fs.write(f'{dayx},{x50},{x200},{xatr},{xrsi},{z},{zx},{tp}\n')
                    print('enter signal!')
                    print('stoploss:',sls)
                    print('profit:',pts)
                    rt.clear()
                    ct.clear()
                   
                elif z < x50:
                    print(z, 'price is lower than', x50, '@',len(ct), 'retries:',len(rt))
                    rt.append(False)



def candle_read(o,c):
    increase = c - o
    percent_diff = increase / o * 100
    return percent_diff

def buy_market_order(mrkt,sl,sl_price,amt_percent=max_trade_amt,us='USDT',min_trade=20,dec=4):

    balance = client.get_asset_balance(asset=us)
    trades = client.get_recent_trades(symbol=mrkt)
    current_amt_avail = float(balance['free'])
    price = float(trades[0]['price'])
    quantity = (current_amt_avail/price)*(amt_percent)
    amt_str = "{:0.0{}f}".format(quantity, dec)

    if current_amt_avail >= min_trade:
        try:
            order = client.order_market_buy(symbol=mrkt, quantity=amt_str)
            sl.append(sl_price)
            print('MARKET BUY! -------->' , 'STATUS : ', order['status'] )
        except:
            print('not enough balance' , balance['free'])
    elif current_amt_avail <= min_trade:
        print('not enough balance' , balance['free'])
 
        


def sell_limit_order(prft,s,mrkt,ordr,sl,amt_percent=0.999,min_trade=20,dec=1):

    if sl:
        balance = client.get_asset_balance(asset=s)
        balance_amt = float(balance['free'])
        trades = client.get_recent_trades(symbol=mrkt)
        trade_value = float(trades[0]['price'])
        quantity = balance_amt * amt_percent
        amt_str = "{:0.0{}f}".format(quantity, dec)
        current_amount_avail = balance_amt * trade_value
        amt_price_str = "{:0.0{}f}".format(prft, dec_price)
        if current_amount_avail <= min_trade:
            print('not enough balance', current_amount_avail)
        elif current_amount_avail > min_trade:
            print(amt_str,amt_price_str,'str and prft')
            order = client.order_limit_sell(symbol=mrkt,quantity=amt_str,price=amt_price_str)
            print('SELL LIMIT ORDER CREATED @ -------->',amt_price_str , order['status'])
            if order['orderId']:
                ord_id = order['orderId']
                ordr.append(ord_id)


def sell_market_order(s,mrkt,stpls,amt_percent=0.999,min_trade=20,dec=4):
    balance = client.get_asset_balance(asset=s)
    balance_amt = float(balance['free'])
    trades = client.get_recent_trades(symbol=mrkt)
    trade_value = float(trades[0]['price'])
    quantity = balance_amt * amt_percent
    amt_str = "{:0.0{}f}".format(quantity, dec)
    current_amount_avail = balance_amt * trade_value


    if current_amount_avail <= min_trade:
        print('not enough balance', current_amount_avail)
    elif current_amount_avail > min_trade:
        order = client.order_market_sell(symbol=mrkt, quantity=amt_str)
        stpls.pop()
        with open('engulfing-trades', 'a') as fs:
            fs.write('False\n')
        print(order)




def cancel_order_stoploss(mrkt,order):
    result = client.cancel_order(symbol=mrkt,orderId=order)
    print(result)

def watch_loss(sl,s,mrkt,dc,bfuc,order):

    if bfuc: 
        
        candle = bfuc.pop()

        if order and sl: 
            candle_closed = float(candle['data']['k']['c'])

            if candle_closed < sl[0] :
                print('stoploss trigerred price is below stop loss ', candle_closed , '-->', sl)
                cancel_order_stoploss(mrkt,order[0])
                order.pop()     
            elif candle_closed > sl[0]:
                print('watching stoploss : ', sl[0])
        
        elif not order and sl:
            sell_market_order(s,mrkt,sl,dec=dc) 


    if order:
        
        try:
            print('checking order')
            check_order = client.get_order(symbol=mrkt,orderId=order[0])
            if check_order['status'] == 'FILLED':
                with open('engulfing-trades', 'a') as fs:
                    fs.write('True\n')       
                orx = order.pop()
                stpx = sl.pop()
                print('order is filled removed stoploss and order',orx,stpx)
        except:
            print('connection error try again')
