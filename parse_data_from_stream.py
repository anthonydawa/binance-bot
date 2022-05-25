import pandas as pd
import datetime as dt
import time
import pickle
import os

label = ['stream', 'data', 'e', 'E', 's', 'k', 't', 'T', 's', 'i', 'f','L','o','c','h','l','v','n','x','q','V','Q','B','p','b','a','m','M']
kline_pd = ['stream', 'data', 'e', 'E', 's', 'k', 't', 'T', 's', 'i', 'f','L','o','c','h','l','v','n','x','q','V','Q','B']
kline_csv = 'stream,data,e,E,s,k,T,s,i,f,L,o,c,h,l,v,n,x,q,V,Q,B'
trade_pd = ['stream','data','e','E','s','t','p','q','b','a','T','m','M']
trade_csv = 'stream,data,e,E,s,t,p,q,b,a,T,m,M'
depth_label =  ['e', 'E', 's','U','u','b','a']

get_date = dt.datetime.now()
now_hour = get_date.hour
now_day = get_date.day

trade_df = pd.DataFrame(columns=['stream', 'data', 'e', 'E', 's', 'k', 't', 'T', 's', 'i', 'f','L','o','c','h','l','v','n','x','q','V','Q','B'])
kline_df = pd.DataFrame(columns=['stream','data','e','E','s','t','p','q','b','a','T','m','M'])

kline_last_data = []

def parse_data_from_stream(data):

    remove_useless_chars = data.replace("{","").replace("}","").replace(':'," ").replace('"',"").replace(',', " ")

    clean_strings = remove_useless_chars.split(' ')
    
    if len(clean_strings) == 4:
        pass
    else: 
        remove_useless_chars = [x for x in clean_strings if len(clean_strings) !=4] 
        dx = [x for x in clean_strings if x not in label]
        sort_data_type(dx)
      
def convert_separator(data):
    add_separator = ""
    for x in data:
        add_separator += "{},".format(x)
    return add_separator

def sort_data_type(data):

    if data[1] == 'kline':
        handle_kline(data)
    elif data[1] == 'trade':
        handle_trade(data)
    else:
        print('not kline or trade data')

def handle_kline(data):
    
    file_name_date = f'kline-{now_hour}-{now_day}.pickle'

    check_file_exist = os.path.exists(file_name_date)

    if check_file_exist:
        seperator = convert_separator(data)
        with open('kline-{}-{}.pickle'.format(now_hour, now_day), 'ab') as f:
            pickle.dump(seperator,f)
    else:
        with open(file_name_date, 'wb') as fp: 
            pass
        pickle.dump(kline_csv,file_name_date)   

def handle_trade(data):

    file_name_date = f'trade-{now_hour}-{now_day}.pickle'
 
    check_file_exist = os.path.exists(file_name_date)

   
    if check_file_exist:
        seperator = convert_separator(data)
        with open('trade-{}-{}.pickle'.format(now_hour,now_day), 'ab') as f:
            pickle.dump(seperator,f)
    else:
        with open(file_name_date, 'wb') as fp: 
            pass
        pickle.dump(trade_csv,file_name_date)

    
# check for kline data if still same do nothing else add data
# def check_new_kline_data(data):




# while True:
#     print(kline_df.tail())
#     print(trade_df.tail())
#     time.sleep(3)