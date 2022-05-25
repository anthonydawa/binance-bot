class MarketOrder:
    def __init__(self,symbol,TP,SL,OrderId):

        self.symbol = symbol
        self.TP = TP
        self.SL = SL
        self.OrderId = OrderId
        self.result = None