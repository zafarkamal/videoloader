class InstrumentDetail:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def override_price(self, new_price):
        self.price = new_price

    def get_instrument_details(self):
        '''
        Returns the details of the instrument.
        '''
        print(f"Instrument Name: {self.name}, Price: {self.price}")

class Trades:
    def __init__(self,instrument,pnl,price):
        self.instrument =  instrument
        self.pnl = pnl
        self.price = price

    def getTradedetails(self):
        '''
        Returns the details of the instrument.
        '''
        print (f"Instrument name {self.instrument},Total PNL {self.pnl},BID price {self.price}")

