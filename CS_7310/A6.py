'''Assignment 6'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
from abc import ABC, abstractmethod

print(" ")

class Shape(ABC):

    def __init__(self,x,y):
        self._x = x
        self._y = y
        self.color = None

    @abstractmethod
    def get_area(self):
        pass

    def set_color(self, color):
        self.color = color

    def set_x(self, x):
        self._x = x

    def set_y(self,y):
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y (self):
        return self._y


print("---")
print("---")
print("---")



'''
1 Write a Triangle class
Start with the abstract class Shape given above.
Write a class Triangle
that is a subclass of Shape
that accepts 4 constructor parameters,
x, y, height and base.
Write code for get_area
in the Triangle class,
where the area is ½ * base * height
Pass the asserts.
'''

# write your Triangle class here...
class Triangle(Shape):
    def __init__(self,x,y,height,base):
        super().__init__(x,y)
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

# create (instantiate) your Triangle object.
# Name it 'myt'
myt = Triangle(2,0,10,10)

# asserts for your Triangle instance
print(myt.get_area() == 50.0)
print(myt.x == 2)
print("Passed OOP1")
print("---")
print("---")
print("---")


'''
2 Write a subclass of Card called Card21
In this assignment
you will create a subclass of card
called Card21
which will have all the features
of your super class Card
PLUS a property called value,
which should return the numeric value
of the card for the game of blackjack.

Use the name of the card
to determine the value.

All numeric cards
should have their face value
(2..10)
Jacks, Queens, Kings
should have value of 10
Ace should have a value of 11
'''

# The Card Class
class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the Card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

# Define Card21 as a subclass of Card
# with a property called 'value'
class Card21(Card):
    def __init__(self, face, suit):
        super().__init__(face, suit)
        self._value = self.calculate_value()

    @property
    def value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def calculate_value(self):
        HIGH_FACES = ['Jack', 'Queen', 'King']
        if super().face in HIGH_FACES:
            self.set_value(10)
        elif super().face == 'Ace':
            self.set_value(11)
        else:
            self.set_value(int(super().face))
        return self.value


# Pass the following asserts
my_card = Card21('Ace','Hearts')
print(my_card.value == 11)

my_card = Card21('Queen','Hearts')
print(my_card.value == 10)

my_card = Card21('2','Hearts')
assert my_card.value == 2
print ("Passed OOP2")
print("---")
print("---")
print("---")

'''
3. Dealer for BlackJack
Create a class called Dealer
that follows the rules of Blackjack.

The constructor should accept one parameter
- call it hand (a list of Card21 objects)

Implement a method called hit_or_stay()
which, based on hand,
returns either 'hit' or 'stay'
depending on the dealer rules.

Dealer Rules
The dealer should return “hit”
if the total value
of all the cards
in the hand
is 16 or less

The dealer should return “stay”
if the total value
of all the cards
in the hand
is 17 or greater

Handling Aces:
The value of the Ace
depends on the dealer's other cards.

Assume the ace is 11 at first.

If the sum of cards with an Ace
adds up to 16 or less,
return 'hit.

If the sum of cards with an Ace
is greater than 17,
return 'stay'.

If the cards have 2 or more aces,
count the first ace as 11
and the others as 1.

If that sum < 17 return 'hit'

Now things get a bit tricky
If after counting the first ace as 11
and the rest as 1,

if the sum > 21,
count the first ace as 1

If the new sum < 17 return 'hit'
else return 'stay'
'''

# Define the Class Dealer
class Dealer():
    def __init__(self, hand):
        self._hand = hand
        self._hand_value = 0
        self._ace_count = 0
        self.update_hand_value_and_ace_count()

    @property
    def hand(self):
        return self._hand

    @property
    def hand_value(self):
        return self._hand_value

    @property
    def ace_count(self):
        return self._ace_count

    def increment_hand_value(self, value):
        self._hand_value += value

    def decrement_hand_value_for_multiple_aces(self, value):
        self._hand_value -= value

    def hit_or_stay(self):
        if self.hand_value <= 16:
            return 'hit'
        else:
            return 'stay'

    def update_hand_value_and_ace_count(self):
        for card in self.hand:
            if card.face == 'Ace':
                self.increment_ace_count()
            self.increment_hand_value(card.value)
        while self.ace_count >= 1 and self.hand_value > 21:
            self.decrement_hand_value_for_multiple_aces(10)
        return self.hand_value

    def increment_ace_count(self):
        self._ace_count += 1


'Dealer class - handling card input'

# Assert
hand = []
hand.append( Card21("Queen", 'Hearts') )
hand.append( Card21("Ace", 'Hearts') )

dealer = Dealer(hand)  # expect 21
print(dealer.hit_or_stay() == 'stay')
print ("Passed OOP3.1")


# Assert 
hand = []
hand.append( Card21("Queen", 'Hearts') )
hand.append( Card21("2", 'Hearts') )

dealer = Dealer(hand)  # expect 12
print(dealer.hit_or_stay() == 'hit')
print ("Passed OOP3.2")


# Assert 
hand = []
hand.append( Card21("Queen", 'Hearts') )
hand.append( Card21("9", 'Hearts') )

dealer = Dealer(hand)  # expect 19
print(dealer.hit_or_stay() == 'stay')
print ("Passed OOP3.3")

#assert with aces - these can be tricky!
hand = []
hand.append( Card21("Queen", 'Hearts') )
hand.append( Card21("2", 'Hearts') )
hand.append( Card21("Ace", 'Hearts') )

dealer = Dealer(hand)  # hand value = 13 counting ace as 1 since 11 goes over 21
print(dealer.hit_or_stay() == 'hit')
print ("Passed OOP3.4")


#Assert with aces
hand = []
hand.append( Card21("Ace", 'Spades') )
hand.append( Card21("2", 'Hearts') )
hand.append( Card21("6", 'Hearts') )
hand.append( Card21("Ace", 'Hearts') )
hand.append( Card21("Ace", 'Hearts') )

dealer = Dealer(hand)  # hand value = 21  one ace=11 other aces=1
print(dealer.hit_or_stay() == 'stay')
print ("Passed OOP3.5")

#Assert with aces -
hand = []
hand.append( Card21("Ace", 'Spades') )
hand.append( Card21("2", 'Hearts') )
hand.append( Card21("6", 'Hearts') )
hand.append( Card21("Ace", 'Hearts') )
hand.append( Card21("Ace", 'Hearts') )
hand.append( Card21("Ace", 'Hearts') )

dealer = Dealer(hand)  # hand value = 12 counting all aces as 1
print(dealer.hit_or_stay() == 'hit')
print ("Passed OOP3.6")
print("---")
print("---")
print("---")