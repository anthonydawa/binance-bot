import time
import threading

market = ['btcusdt','ethusdt']

kline = []

def market_process(kline,market):

    while True:
        if kline:
            k = kline.pop()
            if market == 'btcusdt':
                if k % 2 == 0:
                    print(k,market)
                else:
                    pass 
            elif market == 'ethusdt':
                if k % 2 == 0:
                    pass
                else:
                    print(k,market)
        time.sleep(3)
        print(kline)

for index, _ in enumerate(market):
    t = threading.Thread(target=market_process,args=(kline,market[index]))
    t.start()

count = 0
while True:
    kline.append(count)
    count += 1
    time.sleep(1)


    