

# x = [100.2201,100.23003]


# def roundup(data):
#     for i in data:
#         newx = []
#         newx.append(round(data[i],2))
#     return newx

# print(roundup(x))



# balance = client.get_asset_balance(asset='BNB')

# order = client.create_oco_order(
#     symbol='BNBUSDT',
#     side=SIDE_SELL,
#     quantity=(balance['free']),
#     stopPrice='300.99',
#     price='350.99')

# x=[1,2,3]
# for i in range(3):
#     x.pop()
#     print(x)


# balance = client.get_asset_balance(asset='BNB')
# order = client.create_oco_order(
#     symbol='BNBUSDT',
#     side=SIDE_SELL,
#     stopLimitTimeInForce=10,
#     quantity=balance,
#     stopPrice='242.01',
#     price='242')

# order = client.create_test_order(
#     symbol='BNBBTC',
#     side=SIDE_BUY,
#     type=ORDER_TYPE_LIMIT,
#     timeInForce=TIME_IN_FORCE_GTC,
#     quantity=100,
#     price='0.00001')

# orders = client.get_all_orders(symbol='BTCUSDT', limit=10)
# new_order = ''

# for order in orders:
#     if order['status'] == 'NEW':
#         print(order['orderId'])

# result = client.cancel_order(
#     symbol='BTCUSDT',
#     orderId=5232173857)
# print(result)
# # print(orders)

# balance = client.get_asset_balance(asset='BNB')
# print(balance)

# print(order['orderId'])


# balance = client.get_asset_balance(asset='BTC')
# print(balance)

# klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "3 days ago UTC")
# print(klines)
# print(klines[len(klines)-1][4])




# x = [1,2,3,4]
# print(x[2:])

# x = "1653.6600000"


# print(float(x))


# import pickle

# with open('ETHUSDT_EMA', 'rb') as f:
#     x = pickle.load(f)
#     print(x[3][0])

# x = [1,2,3,4,5,6,7,8,9,10]

# print(x[-3:])

# import numpy as np

# x = np.array([1,2,3,4,5,6,7,8,9,10])
# z = np.array([1,2,3,4,5,6,7,8,9,10])
# a = np.stack([x,z])
# xx = np.append(a,[[11,12],[11,12]],1)
# xy = np.delete(xx,0,1)
# xz = np.append(xy,[[13],[13]],1)
# print(xz)


# from binance.client import Client

# from binance.enums import *


# client = Client('lrX1KTkrceE6IpVoPHfKJTRTL2ngXeo9K5u9o7PmVbpICInXrxa9SBGFyhPj03LM', 'GdW9AV0XjWv5rB9MBR77JfMsxoQ9zSKPX8KyMmXwJKzsoNw1WFevuhmO2r8H8HzU')
# # avg_price = client.get_avg_price(symbol='ADAUSDT')
# # print(avg_price)
 

# fees1 = client.get_trade_fee(symbol='ADAUSDT')
# print(fees1)
# tickers = client.get_ticker()
# prices = client.get_all_tickers()
# print(prices[1])

# from binance.enums import *
# order = client.create_oco_order(
#     symbol='ADAUSDT',
#     side=SIDE_SELL,
#     quantity='1.30747',
#     stopPrice='1.23051',
#     price='1.23050')

# print(order)
# import numpy as np
# from numpy.lib import bartlett

# # x = np.array([[1,2,3,4],[1,2,3,4]])
# # print(x[:,3])

# # y = np.array([[1,2,3],[1,2,3]])

# # a = np.arange(168).reshape((2,7,12))
# # print(a)
# # print(a[:,:,4])

# # x = np.arange(12).reshape((3,4))
# # print(x)
# # y = np.array(x[:,0])
# # print(y)
# # y[0] = 1
# # print(y)
# # print(x)

# x = [1,2]
# x.append(3)
# print(x)

import numpy as np

a = np.arange(80).reshape((2,4,10))
b = [9,8,7,6,5,4,3,2,1,0]

# print(a[0,2:])

def ttt ():
    x = 1
    y = 2
    return x,y

c,v = ttt()


# if new value if not do nothing

# x = [3,2,1,0]

# print(get_index_with_symbol(x,0))



# kline = {'stream': 'bnbusdt@kline_1m', 'data': {'e': 'kline', 'E': 1616681226448, 's': 'BNBUSDT', 'k': {'t': 1616681220000, 'T': 1616681279999, 's': 'BNBUSDT', 'i': '1m', 'f': 187456522, 'L': 187456651, 'o': '234.84670000', 'c': '234.94370000', 
# 'h': '234.94680000', 'l': '234.78820000', 'v': '173.54300000', 'n': 130, 'x': False, 'q': '40761.07918510', 'V': '142.99700000', 'Q': '33586.94620280', 'B': '0'}}}

# x = [2,3,4,5,6]

# if x != []:
#     print(1)
# elif x == []:
#     print(2)


# def xx ():
#     return [1,2,3]

# x = xx()

# print(x)
# x.append(4)
# # print(x)
# x = [1]

# x = 3
# y = 2
# z = y * 2
# # if x <= y:
# #     print('k')



# x = 23.04195259876399 
# y = 22.997599467352792 


# if x < y:
#     print(y)
# if x > y:
#     print(x)
# x = ['21.87550000', '21.76760000', '21.79950000', '21.80020000', '21.83170000', '21.72900000', '21.74750000', '21.76140000', '21.78320000', '21.76910000', '21.76680000', '21.76750000', '21.76610000', '21.58880000', '21.61280000', '21.67420000', '21.63000000', '21.53420000', '21.41370000', '21.29280000', '21.40000000', '21.40950000', '21.40090000', '21.45100000', '21.32710000', '21.47870000', '21.47500000', '21.49400000', '21.48780000', '21.33270000', '21.20990000', '21.26980000', '21.13170000', '21.15000000', '21.15660000', '21.04510000', '21.00920000', '21.08370000', '20.97660000', '20.88690000', '20.69080000', '20.76000000', '20.80940000', '20.78300000', '20.76310000', '20.78540000', '20.84970000', '20.84920000', '21.14300000', '21.20960000', '21.28070000', '21.27410000', '21.40290000', '21.23380000', '21.09410000', '21.15140000', '21.14600000', '21.07240000', '20.95540000', '20.90990000', '20.98100000', '21.00000000', '21.06370000', '21.10320000', '21.20160000', '21.20010000', '21.24430000', '21.26610000', '21.26200000', '21.27850000', '21.24560000', '21.23990000', '21.21760000', '21.18960000', '21.30020000', '21.34340000', '21.33580000', '21.29000000', '21.31010000', '21.34640000', '21.34000000', '21.34640000', '21.30010000', '21.32310000', '21.37240000', '21.32260000', '21.34650000', '21.33280000', '21.39660000', '21.41000000', '21.44670000', '21.46910000', '21.41170000', '21.48970000', '21.50300000', '21.47780000', '21.40190000', '21.38630000', '21.38090000', '21.37630000', '21.49920000', '21.43370000', '21.47110000', '21.49250000', '21.49220000', '21.50000000', '21.51000000', '21.59400000', '21.73210000', '21.74950000', '21.69220000', '21.60960000', '21.68670000', '21.74500000', '21.70900000', '21.63840000', '21.72070000', '21.76730000', '21.76730000', '21.71710000', '21.74450000', '21.81070000', '21.88090000', '21.88100000', '21.89000000', '21.90010000', '21.99990000', '22.00610000', '22.06160000', '22.06790000', '22.09970000', '21.94660000', '22.00180000', '21.94820000', '21.99500000', '21.99000000', '21.82200000', '21.91010000', '21.97000000', '21.90460000', '21.80700000', '21.82890000', '21.91080000', '21.95940000', '21.94400000', '21.86530000', '21.90000000', '21.80250000', '21.73240000', '21.64750000', '21.46950000', '21.45450000', '21.45000000', '21.46590000', '21.46100000', '21.45000000', '21.51080000', '21.46000000', '21.39690000', '21.30750000', '21.38300000', '21.34300000', '21.37520000', '21.48630000', '21.45580000', '21.47660000', '21.47650000', '21.45890000', '21.50950000', '21.51900000', '21.50980000', '21.49300000', '21.47000000', '21.45210000', '21.50000000', '21.50960000', '21.45780000', '21.46210000', '21.53080000', '21.52190000', '21.55090000', '21.63780000', '21.60930000', '21.56880000', '21.69070000', '21.68590000', '21.68790000', '21.76090000', '21.86610000', '21.87200000', '21.91490000', '21.92290000', '21.86420000', '21.87700000', '21.89780000', '21.94970000', '21.95700000', '21.99590000', '21.96870000', '21.95500000', '21.96390000', '21.94980000', '21.83680000', '21.89000000', '21.87250000', '21.65350000', '21.73860000', '21.67850000', '21.78870000', '21.79000000'
# ]


# def ExpMa(values,window):
#     vals=[]
#     for x in values:
#         convert_to_int = float(x)
#         # rounded = round(convert_to_int,4)
#         vals.append(convert_to_int)
#     weights = np.exp(np.linspace(-1.,0.,window))
#     weights /= weights.sum()

#     a = np.convolve(vals,weights,mode='same') [:len(vals)]
#     a[:window] = a[window]
#     return a

# print(ExpMa(x,100))


from binance.client import Client

from binance.enums import *
#t2
apikey = 'utRmBKY2vhRwqqYpDJWcSeEs7O8GeNjCdXhTDNcPtxS02XvSYKGzEiMSTDmYpVtV'
secretkey = 'GArQdPbwTciWECIUNGYBj9oQviJ3IIAZH1PmVopPSAMVE3q7gH4P55aD0QmIn2hC'
client = Client(apikey,secretkey)
    # amount = amt
    # precision = 5
    # amt_str = "{:0.0{}f}".format(amount, precision) 

def buy_market_order(mrkt,amt_percent=0.999,us='USDT',amt=20):

    balance = client.get_asset_balance(asset=us)
    trades = client.get_recent_trades(symbol=mrkt)
    quantity = (float(balance['free']))/float(trades[0]['price'])*(amt_percent)

    if float(balance['free']) >= amt:
        order = client.order_market_buy(symbol=mrkt, quantity=(round(quantity, 4)))
        print(order)
        return order
    elif float(balance['free']) <= amt:
        print('not enough balance' , balance['free'])

def sell_market_order(s,mrkt,amt_percent=0.999,amt=20):

    balance = client.get_asset_balance(asset=s)
    free = float(balance['free'])
    trades = client.get_recent_trades(symbol=mrkt)
    price = float(trades[0]['price'])
    dval = free * price
    qty = float(balance['free'])*amt_percent
    rounded = round(qty,6)
    if dval <= amt:
        print('not enough balance', balance['free'])
    elif dval > amt:
        order = client.order_market_sell(symbol=mrkt, quantity=rounded)
        print(order)
        return order





def sell_limit_order(prft,s,mrkt,amt_percent=0.999,amt=20,dec=1):
    balance = client.get_asset_balance(asset=s)
    free = float(balance['free'])
    trades = client.get_recent_trades(symbol=mrkt)
    price = float(trades[0]['price'])
    dval = free * price
    qty = float(balance['free'])*amt_percent
    rounded = round(qty,dec)
    if dval <= amt:
        print('not enough balance', balance['free'])
    elif dval > amt:
        order = client.order_limit_sell(symbol=mrkt,quantity=rounded,price=prft)
        ord_id = order['orderId']
        print(ord_id)
        return ord_id

# details = client.get_asset_details()
# print(details)

# order = client.order_limit_sell(
#     symbol='ENJUSDT',
#     quantity=44.9,    
#     price=2.6)

# print(order)



# x = {'success': True, 'tradeFee': [{'maker': 0.001, 'symbol': 'ENJUSDT', 'taker': 0.001}]}
# print(x['tradeFee'][0]['maker'])
# sell_limit_order(2.6,'ENJ','ENJUSDT')

#     order = client.order_limit_sell(symbol='BNBBTC',quantity=100,price=prft)


# x = {'symbol': 'BTCUSDT', 'orderId': 5424975258, 'orderListId': -1, 'clientOrderId': 'sWiuJoSHjQ1A1tuumw7odP', 'transactTime': 1617343074212, 'price': '0.00000000', 'origQty': '0.00193200', 'executedQty': '0.00193200', 'cummulativeQuoteQty': '115.11582432', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'SELL', 'fills': [{'price': '59583.76000000', 'qty': '0.00193200', 'commission': '0.00024567', 'commissionAsset': 'BNB', 'tradeId': 741450697}]}


# order = client.order_market_buy(
#     symbol='BTCUSDT',
#     quantity=100)
# {'symbol': 'BTCUSDT', 'orderId': 5424735361, 'orderListId': -1, 'clientOrderId': 'ltwsplryBD5pVw0PmmXami', 'transactTime': 1617340514812, 'price': '0.00000000', 'origQty': '0.00193300', 'executedQty': '0.00193300', 'cummulativeQuoteQty': '115.00449222', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'fills': [{'price': '59495.34000000', 'qty': '0.00193300', 'commission': '0.00024820', 'commissionAsset': 'BNB', 'tradeId': 741386490}]}

# {'symbol': 'ORNUSDT', 'orderId': 78986310, 'orderListId': -1, 'clientOrderId': 'kGuSLey8u2nL5pbD0TDd6P', 'transactTime': 1617243065669, 'price': '25.55550000', 'origQty': '5.60000000', 'executedQty': '0.00000000', 'cummulativeQuoteQty': '0.00000000', 'status': 'NEW', 'timeInForce': 'GTC', 'type': 'LIMIT', 'side': 'SELL', 'fills': []}

def sell_limit_order():
    balance = client.get_asset_balance(asset='ORN')
    x = balance['free']
    order = client.order_limit_sell(
        symbol='ORNUSDT',
        quantity=x,
        price='25.5555')
    print(order)



def check_sell_order():
    order_sell_limit = client.get_all_orders(symbol='ORNUSDT', limit=10)
    latest_order = order_sell_limit[len(order_sell_limit)-1]

    if latest_order['side'] == 'SELL' and latest_order['status'] == 'NEW':
        print('still waiting..')
    elif latest_order['side'] == 'SELL' and latest_order['status'] == 'FILLED':
        print('order is filled')
    elif latest_order['side'] == 'SELL' and latest_order['status'] == 'CANCELED':
        print('order is cancelled')
    else:
        print('something is wrong')







# result = client.cancel_order(
#     symbol='ORNUSDT',
#     orderId=78997734)
# print(result)


# details = client.get_asset_details()
# print(details['assetDetail']['ORN'])

# c = 2.1
# o = 2

# increase = c - o
# x = increase / o * 100
# print(x)

