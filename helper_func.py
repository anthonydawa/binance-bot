
from datetime import datetime

def get_saved_orders():
    order_arr = []
    with open('data/saved_orders','r') as f:

        for line in f.readlines():
            n = line.replace('\n','')
            data = n.split(',')
  
            order_arr.append(data)

    return order_arr
            


def get_completed_orders():

    order_arr = []

    with open('data/completed_orders','r') as f:

        for line in f.readlines():
            n = line.replace('\n','')
            data = n.split(',')     

            order_arr.append(data)

    return order_arr
    

def unconfirmed_orders(arr1,arr2):
    order = []
    for r1 in arr1:

        paired = []

        for r2 in arr2:
            if r1[0] == r2[0] and r1[1] == r2[1]:
                paired.append(True)
            else:
                paired.append(False)
        
        if not True in paired:
            order.append(r1)
                
           
    return order


def return_incomplete_orders():
    return unconfirmed_orders(get_saved_orders(),get_completed_orders())

def get_day_week(ep):
    y = int(ep) / 1000
    x = datetime.fromtimestamp(y).strftime("%A")
    
    for idx,strval in enumerate(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']):
        if strval == x:
            return idx + 1

def get_hour_day(x):
    y = int(x) / 1000
    temp = datetime.utcfromtimestamp(y).strftime('%H')
    fval = ''
    if temp[0] == '0':
        for letters in temp[1:]:
            fval += letters
        return fval
    elif temp[0] != '0':
        return temp



def get_key_from_value(d,val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None

def dict_to_array(d):
    arr = []
    for x in d:
        arr.append(d[x])
    return arr

def return_timeframe_minute(x):
    if x == '15m':
        return 15
    elif x == '4h':
        return 60 * 4
    elif x == '1h':
        return 60
    elif x == '1d':
        return 60 * 24
