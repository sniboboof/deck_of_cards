import random


#global card name translations for string inputs
#to save time and memory from making a dictionary every time a card is made
CARD_VALUES_SPECIAL_NAMES = {
    'Ace': 1, 'Jack': 11, 'Queen': 12, 'King': 13
}
CARD_VALUES_SPECIAL_NAMES_REVERSE = {
    v: k for k, v in CARD_VALUES_SPECIAL_NAMES.items()
}

CARD_SUITS = {
    0: 'Clubs', 1: 'Diamonds', 2: 'Hearts', 3: 'Spades'
}


#individual cards
#a hand is basically a list of cards
#a deck is basically a d.e.queue
class Card():
    def __init__(self, value=None, suit=None):
        #assumes 4 suits and 13 values when determining identity randomly
        #but if values and suits are specified (and the suit is defined)
        #any number of either can be used
        if value is None:
            value = random.randrange(1, 14)
        if suit is None:
            suit = random.randrange(0, 4)

        #value can be given either as a string or an int
        myValue = None
        if isinstance(value, str):
            try:
                myValue = CARD_VALUES_SPECIAL_NAMES[value.capitalize()]
            except KeyError:
                myValue = int(value)
        elif isinstance(value, int):
            myValue = value
        else:
            raise TypeError
        self.value = myValue

        mySuit = None
        if isinstance(suit, str):
            if suit.capitalize() in CARD_SUITS.values():
                mySuit = suit.capitalize()
            else:
                raise KeyError
        elif isinstance(suit, int):
            mySuit = CARD_SUITS[suit]
        else:
            raise TypeError
        self.suit = mySuit

    def __str__(self):
        start = ""
        try:
            start = CARD_VALUES_SPECIAL_NAMES_REVERSE[self.value]
        except KeyError:
            start = str(self.value)

        middle = " of "

        end = self.suit

        return start+middle+end

    def __cmp__(self, opponent):
        if isinstance(opponent, Card):
            return self.value.__cmp__(opponent.value)
        else:
            return NotImplemented


#designed to behave like a real deck
#it is kindof needlessly complex for a real game of cards
#so the model for useful functions is based more on
#card tricks and dirty dealing

#think of bottom and front (0 index) of deck as the same (the face out side)
#think of top and back (max index) of deck the same (face in side)

#two functions have hidden booleans to change normal behavior
#they can be used to covertly give people a known card
class Deck():
    def __init__(self, cards):
        pass

    def __len__(self):
        pass

    def shuffle(self):
        pass

    def sort(self):
        pass

    #reveal functions show a card without modifying the deck
    #like a real deck, if you don't want information about the card's location
    #you have to shuffle afterwards
    def topDeck(self):
        pass

    def botDeck(self):
        pass

    def cut(self):
        pass

    #the only function that reduces deck size
    #has a hidden overload
    def deal(self, count=1, bottom=False):
        pass

    #the two ways to put cards back into the deck
    #put has a hidden overload to put cards on top instead of where they belong
    def put(self, cards, top=False):
        pass

    def shuffleIn(self, cards):
        pass
