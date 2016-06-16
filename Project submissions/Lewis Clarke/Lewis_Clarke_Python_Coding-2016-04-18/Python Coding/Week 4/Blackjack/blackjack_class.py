class Bankroll(object):

    def __init__(self,bank= 100):
        self.bank = bank

    def place_bet(self,bank):
        bet = int(raw_input('Enter bet amount: '))
        print ('You placed a bet of'),bet
        self.bank -= bet
        return self.bank

    def get_bankroll(self):
        print self.bank


    def new_bankroll(self,bank):
        self.bank = bank
        
