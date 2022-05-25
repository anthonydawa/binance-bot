label = ['stream', 'data', 'e', 'E', 's', 'k', 't', 'T', 's', 'i', 'f','L','o','c','h','l','v','n','x','q','V','Q','B','p','b','a','m','M']


def parse_data_from_stream(data):

    remove_useless_chars = data.replace("{","").replace("}","").replace(':'," ").replace('"',"").replace(',', " ")

    clean_strings = remove_useless_chars.split(' ')
    
    if len(clean_strings) == 4:
        pass
    else: 
        remove_useless_chars = [x for x in clean_strings if len(clean_strings) !=4] 
        dx = [x for x in clean_strings if x not in label]
        print(dx)
        
        with open('kline_15m_latest', 'a') as f:
            f.write(dx)