first_entry = False
first_exit = False
second_entry = False
second_exit = False

strat_loop = [first_entry,first_exit,second_entry]

def price_tracker(current_price,target_price,condition):
    #get ema200 first
    if condition == 'enter':
        if current_price > target_price:
            first_entry = True
            print('entered')
        else:
            print('not yet entered')
    elif condition == 'exit':
        if current_price < target_price:
            print('exit')
        else:
            print('not yet exited')

