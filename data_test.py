from numpy.lib.arraysetops import unique


class Data:
    def __init__(self,symbol,csv_path,period):
        self.symbol = symbol.upper()
        self.period = period
        self.csv_path = csv_path
        self.kline_period = self.get_kline_period()
        self.isolated_test = self.get_isolated_test()
        # self.shared_test = None

        # print(self.kline_period)
        # print(self.isolated_test)
        


    def get_isolated_test(self): 
        from os import listdir
        from os.path import isfile, join
        import csv

        onlyfiles = [f for f in listdir('backtest_data_isolated') if isfile(join('backtest_data_isolated', f))]
        targetfiles = [f for f in onlyfiles if self.symbol in f]
        if targetfiles:
            with open(f'backtest_data_isolated/{targetfiles[0]}', newline='') as csvfile:

                data = list(csv.reader(csvfile, delimiter=','))

                q_kline = [x for x in data if int(x[0]) >= int(self.kline_period)]

                return q_kline

                  
    def get_shared_test(self):
        pass

    def get_kline_period(self):

        from os import listdir
        from os.path import isfile, join
        import pickle

        onlyfiles = [f for f in listdir('historical_klines') if isfile(join('historical_klines', f))]
        targetfiles = [f for f in onlyfiles if self.symbol in f and '1d' in f]
        tfile = targetfiles[0]
     
        with open(f'historical_klines/{tfile}','rb') as f:
            kline_from_file = pickle.load(f)
            latest_time_from_kline = kline_from_file[-1][0]
            start_period =  latest_time_from_kline - (86400000 * self.period)
            return start_period

    def compute_method_weight(self):

        import collections

        #d,o,h,l,c,TP,SL,rr1,rr2,Trend,result,method,dayweek,hourday,timeframe

        start_time = self.kline_period
        time_intervals =  [ (x * 86400000 + start_time) for x in range(self.period) ]
        qualified_method_list = [ [] for _ in range(self.period) ]
        all_list = []
        ft = lambda x : f'{x[7]},{x[8]},{x[9]},{x[11]},{x[14]}'
    
        for idx, x in enumerate(time_intervals):
            for y in self.isolated_test:
                # check values within the range and appends to list
                if int(x) <= int(y[0]) < int(x) + 86400000 and int(y[10]) == 1 and float(y[5]) > float(y[6]):
                    qualified_method_list[idx].append(ft(y))
                    all_list.append(ft(y))

        unique_list = list(set(all_list))
        counter_list = collections.Counter(all_list)

        print(counter_list)
        

            
        

x = Data('BTCUSDT','backtest_data_isolated\BTCUSDT-5 May 2013-17 June 2021.csv',14)

x.compute_method_weight()


        
            
