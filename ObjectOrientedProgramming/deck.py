'''deck.py'''
import random
print(" ")

class Deck:
    '''Deck'''
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2,11) + ["J", "Q", "K", "A"]]

    def __init__(self): 
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        '''fill_deck'''
        for suit in Deck.suits:
            for value in Deck.values:
                card = value + suit
                self.cards.append(card)


    def shuffle(self):
        '''shuffle'''
        random.shuffle(self.cards)

    def deal(self, n):
        '''deal'''
        dealt_card = []

        for i in range(n):
            if len(self.cards) == 0:
                break

            card = self.cards.pop()
            dealt_card.append(card)

        return dealt_cards

    def sort_by_suit(self):
        '''sort_by_suit'''
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            suit = card[-1]
            cards_by_suit[suit].append(card)
        
        self.cards = (
            cards_by_suit["H"] + 
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"]
        )

    def contains(self, card):
        '''contains'''
        return card in self.cards

    def copy(self):
        '''copy'''
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        return new_deck

    def get_cards(self):
        '''get_cars'''
        return self.cards[:]

    def __len__(self):
        return len(self.cards)


print(" ")