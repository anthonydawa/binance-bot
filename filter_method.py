
from pattern_indicator import pattern_indicator


def return_best_methods (market_csv,win_limit=50,gain_limit=150):
    upper = str(market_csv).upper()  

                                   
    try:

        csv_file = f'RESULTS/{upper}-RESULTS.csv'

        with open(csv_file,'r') as f:
            file = f.readlines()

        line_arr = []
        for lines in file:
            line = lines.split(",")
            if float(line[0]) >= win_limit and float(line[-1]) >= gain_limit:
                line_arr.append(line)
            else:
                pass

        method_arr = []
        methods = []
        final = []

        for line in line_arr:
            if line[-2] not in method_arr:
                method_arr.append(line[-2])

        for _ in method_arr:
            methods.append([])  
            
        for line in line_arr:
            if line[-2] in method_arr:
                idx = method_arr.index(line[-2])
                methods[idx].append(line)

        def sort_by_timeframe(arr):
            tf_arr = ['5m','15m','1h','4h']
            tfs_arr = [[],[],[],[]]

            for x in arr:
                if x[6] in tf_arr:
                    idx = tf_arr.index(x[6])
                    tfs_arr[idx].append(x)
            return tfs_arr

        def order_by_gains(arr):

            if len(arr) == 1:
                return arr[0]
            elif len(arr) > 1:
                highest = 0
                value = []
                for x in arr:
                    strx = str(x[-1])
                    newx = strx.replace('\n','')
                    if float(newx) > highest:
                        highest = float(newx)
                        if value:
                            value.pop()
                        value.append(x)    
                    elif float(newx) < highest:
                        pass
                return value[0]

        for method in methods:
            sorted = sort_by_timeframe(method)
            for s in sorted:
                x = order_by_gains(s)
                if x:
                    final.append(x)

        return final, upper
    except:
        return [] , upper




def return_best_by_timeframe(symbol,timeframex):


    best_methods, _ = return_best_methods(symbol)

    methods_5m = []
    methods_15m = []
    methods_1h = []
    methods_4h = []

    for arr in best_methods:
        timeframe = arr[6]
        method_num = pattern_indicator[int(arr[-2])]
        risk_win = arr[4]
        risk_loss = arr[5]
        gains = arr[-1].replace('\n','')
        formatx = [method_num,risk_win,risk_loss,gains]


        if timeframe == '5m':
            methods_5m.append(formatx)
        elif timeframe == '15m':
            methods_15m.append(formatx)
        elif timeframe == '1h':
            methods_1h.append(formatx)
        elif timeframe == '4h':
            methods_4h.append(formatx)

    if timeframex == '5m':
        return methods_5m
    elif timeframex == '15m':
        return methods_15m
    elif timeframex == '1h':
        return methods_1h
    elif timeframex == '4h':
        return methods_4h
