import random
from copy import deepcopy
from collections import deque


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
    def __init__(self, cards=None):
        if cards is None:
            self.cards = deque()
            for soot in xrange(4):
                for valoo in xrange(1, 14):
                    self.cards.append(Card(valoo, soot))
        else:
            self.cards = deque(cards)

    def __len__(self):
        return len(self.cards)

    def __eq__(self, other):
        if isinstance(other, Deck):
            return self.cards == other.cards
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Deck):
            return not (self.cards == other.cards)
        else:
            return NotImplemented

    def shuffle(self):
        # have to convert cards to a list or shuffling is too slow
        tempCards = list(self.cards)
        random.shuffle(tempCards)
        self.cards = deque(tempCards)

    def sort(self):
        tempCardSuits = {}
        for card in self.cards:
            tempCardSuits.setdefault(card.suit, [])
            tempCardSuits[card.suit].append(card)

        for key in tempCardSuits.keys():
            tempCardSuits[key].sort()

        self.cards = deque()
        for i in xrange(len(CARD_SUITS.keys())):
            for card in tempCardSuits.get(CARD_SUITS[i], []):
                self.cards.append(card)

    #reveal functions show a card without modifying the deck
    #like a real deck, if you don't want information about the card's location
    #you have to shuffle afterwards
    def topDeck(self):
        return str(self.cards[-1])

    def botDeck(self):
        return str(self.cards[0])

    def cut(self):
        #this function is slower than actual cutting, O(n)
        return str(self.cards[random.randrange(len(self))])

    #the only function that reduces deck size
    #has a hidden overload to deal from the bottom instead of the top
    def deal(self, count=1, bottom=False):
        hand = []
        if count > len(self):
            raise IndexError
        if bottom:
            for i in xrange(count):
                hand.append(self.cards.popleft())
        else:
            for i in xrange(count):
                hand.append(self.cards.pop())
        return hand

    #the two ways to put cards back into the deck
    #put has a hidden overload to put cards on top instead of where they belong
    def put(self, hand, top=False):
        if top:
            self.cards.extend(hand)
        else:
            hand.reverse()
            self.cards.extendleft(hand)

    def shuffleIn(self, hand):
        hand = deque(hand)
        #preserves order of the deck
        #and the order of the cards shuffled into the deck
        insertPoints = sorted(random.sample(range(len(self)), len(hand)))
        insertPoints = deque(insertPoints)

        #startPointer tracks where the bottom of the deck is
        #if we're inserting to 0, then the bottom of the deck changes
        startPointer = None
        if insertPoints[0] == 0:
            self.cards.appendleft(hand.popleft())
            startPointer = self.cards[0]
            self.cards.rotate(-1)
            insertPoints.popleft()
        else:
            startPointer = self.cards[0]

        #main loop goes through each insert point
        #rotates the deck to the right point
        #and puts the card on the bottom
        prevInsert = 0
        for insert in insertPoints:
            self.cards.rotate(-1 * (insert-prevInsert-1))
            self.cards.appendleft(hand.popleft())
            prevInsert = insert

        #finally, return the list back to where it was
        #alternatively i could have just mathed the last insert with some lens
        while self.cards[0] is not startPointer:
            self.cards.rotate(-1)
