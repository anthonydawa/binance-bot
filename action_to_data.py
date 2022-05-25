import pickle 
def action_to_data():
    data = []
    with open('dogebtc.pickle', 'rb') as fr:
        try:
            while True:
                data.append(pickle.load(fr))
        except EOFError:
            pass
    print(data)

action_to_data()