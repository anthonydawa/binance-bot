
x = ['streamxrpdownusdt@kline_1mdataeklineE1612615040806sXRPDOWNUSDTkt1612615020000T1612615079999sXRPDOWNUSDTi1mf3046133L3046146o0.00523800c0.00524000h0.00524000l0.00523800v2266917.34000000n14xfalseq11878.38448014V2266917.34000000Q11878.38448014B0']
y = ['stream', 'srmbtc@kline_1m', 'data', 'e', 'kline', 'E', '1612615219292', 's', 'SRMBTC', 'k', 't', '1612615200000', 'T', '1612615259999', 's', 'SRMBTC', 'i', '1m', 'f', '2810354', 'L', '2810354', 'o', '0.00007137', 'c', '0.00007137', 'h', '0.00007137', 'l', '0.00007137', 'v', '14.00000000', 'n', '1', 'x', 'false', 'q', '0.00099918', 'V', '0.00000000', 'Q', '0.00000000', 'B', '0']
# def parse_line_data(data):
#         data_to_str = str(data)
#         remove_useless_chars = data_to_str.replace("{","").replace("}","").replace(':',"").replace(",","").replace("'","")
#         make_array_of_strings = remove_useless_chars.split(' ')
#         array_of_strings = []
#         for string in make_array_of_strings:
#             array_of_strings.append(string)
#         return array_of_strings

# with open('data_lines', 'r') as f:
#     x = f.readlines()[4]
#     y = parse_line_data(x)
#     print(x)

# {"stream":"powrbtc@kline_1m","data":{"e":"kline","E":1612595883726,"s":"POWRBTC","k":{"t":1612595820000,"T":1612595879999,"s":"POWRBTC","i":"1m","f":9563483,"L":9563516,"o":"0.00000397","c":"0.00000399","h":"0.00000400","l":"0.00000397","v":"17526.00000000","n":34,"x":true,"q":"0.06987855","V":"14684.00000000","Q":"0.05858473","B":"

with open('x', 'w') as f:
    f.write('123')