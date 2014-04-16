import random


#individual cards
#a hand is basically a list of cards
#a deck is basically a d.e.queue
class Card():
    def __init__(self, value, suit):
        pass

    def __str__(self):
        pass

    def __cmp__(self, operand):
        pass


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
