deck_of_cards
=============

a simple exercise in object-oriented design. Sort-of for Code Fellows but mostly just for fun at this point.

contains Card object and Deck object
Card has a suit and value, Deck is a deque of Cards with special functions attached
lists of cards can be used to imitate hands, although maybe another object could also be created for that purpose

the default deck is a standard poker deck. suits and values can be changed by altering the CARD_VALUES_SPECIAL_NAMES and CARD_SUITS globals, for instance if you wanted to make a tarot deck. although you will have to either alter the __init__ method or construct the list of cards you want and pass it in to the constructor if you want a deck that isn't 52 cards divided into 4 suits with 13 values per suit.

most functions in this deck DO NOT perfectly simulate a random deck, they are meant to simulate a physical deck.

revealing cards from the top, bottom, and middle do not mutate the deck and therefore reveal information about the deck if it is not shuffled afterwards

dealing cards from and placing cards into the deck have hidden overloads to deal and place cards on the wrong side of the deck, this allows the deck to "perform tricks"

if you want this to simulate a deck that would be ideal for casino use (no  knowledge of the order of the deck's contents) then you need to .shuffle() when you put cards back on the deck, shuffling into is not enough.
