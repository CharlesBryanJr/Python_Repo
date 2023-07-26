'''game.py'''
from deck import Deck
from hand import Hand

class Game:
    '''Game'''

    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        '''start_game'''