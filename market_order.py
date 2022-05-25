from binance.enums import *
# from binance.helpers import round_step_size
from binance.client import Client
from binance.enums import *
from credentials import apikey, secretkey

client = Client(apikey,secretkey)


def count_decimal(num):
    str_num = str(num)
    count = 0
    for d in str_num:
        if d == '0':
            count += 1
        elif d == '.':
            pass
        elif d == '1':
            break
    return count


def get_lot_size(symbol):
    details = client.get_symbol_info(str(symbol).upper())
    lot_size = count_decimal(details['filters'][0]['tickSize'])
    return lot_size

def get_price_filter(symbol):
    details = client.get_symbol_info(str(symbol).upper())
    price_filter = count_decimal(details['filters'][2]['stepSize'])
    return price_filter

def buy_limit_order(symbol,TP,lot_size,price_filter,min_trade = 11):

    balance = client.get_asset_balance(asset='USDT')
    balance_amt = float(balance['free'])
    amt_price_str = "{:0.0{}f}".format(TP, price_filter)  
    quantity = balance_amt * 0.999
    amt_str = "{:0.0{}f}".format(quantity, lot_size)
    trades = client.get_recent_trades(symbol=symbol)
    trade_value = float(trades[0]['price'])
    current_amount_avail = balance_amt * trade_value  

    if current_amount_avail < min_trade:
        print('not enough balance', current_amount_avail)
    elif current_amount_avail >= min_trade:
        success = False
        count = 0
        while success == False:
            try:
                client.order_limit_buy(symbol=str(symbol).upper(),quantity=amt_str,price=amt_price_str)
            except:
                if count == 3:
                    success = True
                else:
                    count += 1
                    print('error buy_limit_order',symbol,'trying again..')


def sell_limit_order(symbol,TP,lot_size,price_filter,min_trade = 11): 
    strx = str(symbol).replace('USDT','')

    balance = client.get_asset_balance(asset=strx)
    balance_amt = float(balance['free'])
    quantity = balance_amt * 0.999
    amt_str = "{:0.0{}f}".format(quantity, lot_size)
    amt_price_str = "{:0.0{}f}".format(TP, price_filter)
    trades = client.get_recent_trades(symbol=symbol)
    trade_value = float(trades[0]['price'])
    current_amount_avail = balance_amt * trade_value

    if current_amount_avail < min_trade: 
        
        print('not enough balance', current_amount_avail)

    elif current_amount_avail >= min_trade:
        success = False
        count = 0
        while success == False:
            try:
                order = client.order_limit_sell(symbol=symbol,quantity=amt_str,price=amt_price_str)
                return order['orderId']
            except:
                if count == 3:
                    success = True
                else:
                    count += 1
                    print('error sell_limit_order',symbol,'trying again..')




def buy_market_order(symbol,lot_size,min_trade = 11):

    balance = client.get_asset_balance(asset='USDT')
    trades = client.get_recent_trades(symbol=symbol)
    current_amt_avail = float(balance['free'])
    price = float(trades[0]['price'])
    quantity = (current_amt_avail/price)*(0.99)
    amt_str = "{:0.0{}f}".format(quantity, lot_size)
    
    if current_amt_avail >= min_trade:
        success = False
        count = 0
        while success == False:
            try:
                order = client.order_market_buy(symbol=symbol, quantity=amt_str)
                return order['orderId']
            except:
                if count == 3:
                    success = True
                else:
                    count += 1
                    print('error buy_market_order',symbol,'trying again..')

    elif current_amt_avail < min_trade:
        print('not enough balance' , balance['free'])




def sell_market_order(symbol,lot_size,min_trade = 11): 

    strx = str(symbol).replace('USDT','')
    balance = client.get_asset_balance(asset=strx)
    balance_amt = float(balance['free'])
    trades = client.get_recent_trades(symbol=symbol)
    trade_value = float(trades[0]['price'])
    quantity = balance_amt * 0.999
    amt_str = "{:0.0{}f}".format(quantity, lot_size)
    current_amount_avail = balance_amt * trade_value

    if current_amount_avail <= min_trade:
        print('not enough balance', current_amount_avail)
    elif current_amount_avail > min_trade:
        success = False
        count = 0
        while success == False: 
            try:               
                client.order_market_sell(symbol=symbol, quantity=amt_str)
            except:
                if count == 3:
                    success = True
                else:
                    count += 1
                    print('error sell_market_order',symbol,'trying again..')


