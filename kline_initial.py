
from binance.client import Client
from binance.enums import *
from credentials import apikey, secretkey




client = Client(apikey,secretkey)

def klines_initial(symbol,timeframe,limit_candles):
    retries = 0
    while retries < 3:
        try:
            upper = str(symbol.upper())
            if timeframe == '1m':
                candles = client.get_historical_klines(upper, Client.KLINE_INTERVAL_1MINUTE, "1 days ago UTC")
            elif timeframe == '5m':
                candles = client.get_historical_klines(upper, Client.KLINE_INTERVAL_5MINUTE, "2 days ago UTC")
            elif timeframe == '15m':
                candles = client.get_historical_klines(upper, Client.KLINE_INTERVAL_15MINUTE, "3 days ago UTC")
            elif timeframe == '1h':
                candles = client.get_historical_klines(upper, Client.KLINE_INTERVAL_1HOUR, "4 days ago UTC")
            elif timeframe == '4h':
                candles = client.get_historical_klines(upper, Client.KLINE_INTERVAL_4HOUR, "11 days ago UTC")
            elif timeframe == '1d':
                candles = client.get_historical_klines(upper, Client.KLINE_INTERVAL_1DAY, "60 days ago UTC")

            candles.remove(candles[-1])
            limited_candles = candles[-limit_candles:]
            final = []
            for c in limited_candles:
                dx = int(c[0])
                ox = float(c[1])
                hx = float(c[2])
                lx = float(c[3])
                cx = float(c[4])
                kx = [dx,ox,hx,lx,cx]
                final.append(kx)

            return final

        except:
            retries += 1




# print(klines_initial('btcusdt','5m',50))
# "5m = 300000"
# "15m = 900000"
# "1h = 3600000"
# "4h = 14400000"

# 1621158600000
# # 1620964187823

# {'stream': 'btcusdt@kline_5m', 'data': {'e': 'kline', 'E': 1621161000028, 's': 'BTCUSDT', 'k': {'t': 1621160700000, 'T': 1621160999999, 's': 'BTCUSDT', 'i': '5m', 'f': 836714065, 'L': 836719689, 'o': '49300.03000000', 'c': '49444.22000000', 'h': '49462.26000000', 'l': '49277.00000000', 'v': '186.20448000', 'n': 5625, 'x': True, 'q': '9193378.40726126', 'V': '98.34734900', 'Q': '4856120.97263099', 'B': '0'}}}

# 1621159500000
# 1621159800000
# 1621159800000
# 1621159800000


# 1621159800000, '2.38400000', '2.39280000', '2.37810000', '2.39130000',
# 1621159800000, '2.38400000', '2.39280000', '2.37810000', '2.39110000',
# 1621159800000, '2.38400000', '2.39330000', '2.37810000', '2.39270000',