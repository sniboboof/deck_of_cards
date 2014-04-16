import unittest
from pokerdeck import Deck, Card, CARD_SUITS
from copy import copy


class CardCase(unittest.TestCase):

    def testConstruct(self):
        randCard = Card()
        assert randCard is not None
        assert randCard.value in range(1, 14)
        assert randCard.suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']

        def tryspecific(val, soot):
            specificCard = Card(val, soot)
            self.assertEqual(specificCard.value, val)
            self.assertEqual(specificCard.suit, CARD_SUITS[soot])

        for item in ((7, 2), (12, 0), (1, 3), (2, 1)):
            tryspecific(*item)

    def testDifficultConstruct(self):
        specificCard = Card('queen', 1)
        self.assertEqual(specificCard.value, 12)

        specificCard = Card('Ace', 3)
        self.assertEqual(specificCard.value, 1)

        specificCard = Card('KING', 2)
        self.assertEqual(specificCard.value, 13)

        for suitstring in ('clubs',
                           'Diamonds',
                           'HEARTs',
                           'sPadEs'):
            specificCard = Card(3, suitstring)
            self.assertEqual(specificCard.value, 3)
            self.assertEqual(specificCard.suit, suitstring.capitalize())

    def testOperators(self):
        # keep in mind: suits are not considered in value

        # equality
        self.assertTrue(Card(1, 1) == Card(1, 1))
        self.assertFalse(Card(2, 2) == Card(1, 1))
        self.assertTrue(Card(1, 1) == Card(1, 3))
        self.assertFalse(Card(2, 0) == Card(7, 0))

        # greater than/less than
        self.assertTrue(Card(1, 1) < Card(12, 1))
        self.assertTrue(Card(3, 0) >= Card(3, 0))
        self.assertFalse(Card(1, 1) > Card(12, 1))
        self.assertFalse(Card(7, 2) <= Card(1, 0))

    def testString(self):
        assert "of" in str(Card())
        self.assertEqual("Jack of Clubs", str(Card("jack", "clubs")))
        self.assertEqual("4 of Diamonds", str(Card(4, "diamonds")))


class DeckCase(unittest.TestCase):

    def testConstruct(self):
        mydek = Deck()
        assert mydek is not None
        self.assertEqual(mydek.cards[0], Card(1, 0))
        self.assertEqual(mydek.cards[51], Card(13, 3))
        self.assertRaises(IndexError, mydek.cards.get(52))

        smalldek = Deck([Card(1, 0)])
        assert smalldek is not None
        self.assertEqual(smalldek.cards[0], Card(1, 0))
        self.assertRaises(IndexError, smalldek.cards.get(1))

        meddek = Deck([Card(1, 0), Card('Queen', 'Hearts'), Card(1, 0)])
        self.assertEqual(meddek.cards[0], meddek.cards[2])
        self.assertEqual(meddek.cards[2], Card(1, 0))
        self.assertEqual(meddek.cards[1], Card('Queen', 'Hearts'))

    def testCount(self):
        mydek = Deck()
        self.assertEqual(len(mydek), 52)

        mydek = Deck([Card(1, 0), Card('Queen', 'hearts'), Card(1, 0)])
        self.assertEqual(len(mydek), 3)

    def testShuffleSort(self):
        mydek = Deck()
        imitation = copy(mydek)
        mydek.shuffle()
        self.assertNotEqual(mydek, imitation)
        mydek.sort()
        self.assertEqual(mydek, imitation)

    def testCut(self):
        mydek = Deck([Card('ace', 'clubs')])
        imitation = copy(mydek)
        self.assertEqual(mydek.cut(), 'Ace of Clubs')
        self.assertEqual(mydek, imitation)

        mydek = Deck()
        imitation = copy(mydek)
        assert 'of' in mydek.cut()
        self.assertEqual(mydek, imitation)

    def testTopDeck(self):
        mydek = Deck([Card('Queen', 'Hearts')])
        imitation = copy(mydek)
        self.assertEqual(mydek.topDeck(), 'Queen of Hearts')
        self.assertEqual(mydek, imitation)

        mydek = Deck()
        imitation = mydek
        self.assertEqual(mydek.topDeck(), 'King of Spades')
        self.assertEqual(mydek, imitation)

    def testBottomDeck(self):
        mydek = Deck([Card('Queen', 'Hearts')])
        imitation = copy(mydek)
        self.assertEqual(mydek.botDeck(), 'Queen of Hearts')
        self.assertEqual(mydek, imitation)

        mydek = Deck()
        imitation = mydek
        self.assertEqual(mydek.botDeck(), 'Ace of Clubs')
        self.assertEqual(mydek, imitation)

    def testDeal(self):
        mydek = Deck([])
        self.assertRaises(IndexError, mydek.deal())

        mydek = Deck([Card('queen', 'hearts')])
        myhand = []
        self.assertRaises(IndexError, mydek.deal(2))
        myhand.append(mydek.deal())
        self.assertEqual(myhand[0], Card('queen', 'hearts'))
        assert myhand[0] not in mydek.cards
        self.assertEqual(len(myhand), 51)

        mydek = Deck()
        myhand = []
        myhand.append(mydek.deal(2))
        self.assertEqual(myhand, [Card('king', 'spades'),
                                  Card('queen', 'spades')])

        #if they find out this overload exists, you could get shot
        mydek = Deck()
        myhand = []
        myhand.append(mydek.deal(2, True))
        self.assertEqual(myhand, [Card('ace', 'clubs'),
                                  Card('2', 'clubs')])

    def testPutTopBot(self):
        start = [Card('queen', 'hearts')]
        mydek = Deck(copy(start))

        toTop = [Card('ace', 'spades'), Card('king', 'hearts')]
        mydek.put(copy(toTop), True)

        toBot = [Card('1', 'clubs'), Card('2', 'clubs')]
        mydek.put(copy(toBot))

        self.assertEqual(len(mydek), 5)
        self.assertEqual(mydek.cards, toBot+start+toTop)

    def testShuffleIn(self):
        mydek = Deck()
        imitation = copy(mydek)
        mydek.deal(2)
        mydek.shuffleIn([Card('king', 'spades'),
                         Card('queen', 'spades')])
        self.assertNotEqual(mydek, imitation)
        mydek.sort()
        self.assertEqual(mydek, imitation)


if __name__ == "__main__":
    unittest.main()
