class Bankroll(object):

    def __init__(self,bank= 100):
        self.bank = bank

    def place_bet(self,bank):
        bet = int(raw_input('Enter bet amount: '))
        print ('You placed a bet of'),bet
        self.bank -= bet
        print ('Your balance is:'), self.bank

    def get_bankroll(self):
        print self.bank


    def new_bankroll(self,bank):
        self.bank = bank

bankroll = Bankroll()
from random import randint
import random
def hand():
    suits = ['Hearts', 'Dimonds', 'Clubs', 'Spades']
    deal1 = randint(1,13)
    if deal1 == 1:
        print ('Ace'), ('Of'), (random.choice(suits))
    elif deal1 == 11:
        print ('Jack'), ('Of'), (random.choice(suits))
    elif deal1 == 12:
        print ('Queen'), ('Of'), (random.choice(suits))
    elif deal1 == 13:
        print ('King'), ('Of'), (random.choice(suits))
    else:
        print deal1, ('Of'), (random.choice(suits))
    deal2 = randint(1,13)
    suits = ['Hearts', 'Dimonds', 'Clubs', 'Spades']
    if deal2 == 1:
        print ('Ace'), ('Of'), (random.choice(suits))
    elif deal2 == 11:
        print ('Jack'), ('Of'), (random.choice(suits))
    elif deal2 == 12:
        print ('Queen'), ('Of'), (random.choice(suits))
    elif deal2 == 13:
        print ('King'), ('Of'), (random.choice(suits))
    else:
        print deal2, ('Of'), (random.choice(suits))
    print ('Your hand equals:'), deal1+deal2

while True:
    bankroll.place_bet(1)
    deal = raw_input('Press D to deal or Q to quit the game: ')
    if deal == ('d' or 'D'):
        hand()
        break
    elif deal == ('q' or 'Q'):
        print ('Thank you for playing')
        break
    else:
        print ('That input is not valid')
        continue
