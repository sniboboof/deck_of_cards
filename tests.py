import unittest
from pokerdeck import Deck, Card


class CardCase(unittest.TestCase):

    def testConstruct(self):
        randCard = Card()
        assert randCard is not None
        assert randCard.value in range(1, 14)
        assert randCard.suit in range(4)

        self.assertRaises(IndexError, Card(value=0))
        self.assertRaises(IndexError, Card(value=14))
        self.assertRaises(IndexError, Card(suit=-1))
        self.assertRaises(IndexError, Card(suit=4))

        def tryspecific(val, soot):
            specificCard = Card(val, soot)
            self.assertEqual(specificCard.value, val)
            self.assertEqual(specificCard.suit, soot)

        for item in ((7, 2), (12, 0), (1, 3), (2, 1)):
            tryspecific(*item)

    def testDifficultConstruct(self):
        specificCard = Card('queen', 1)
        self.assertEqual(specificCard.value, 12)
        self.assertEqual(specificCard.suit, 1)

        specificCard = Card('Ace', 3)
        self.assertEqual(specificCard.value, 1)
        self.assertEqual(specificCard.suit, 3)

        specificCard = Card('KING', 2)
        self.assertEqual(specificCard.value, 13)
        self.assertEqual(specificCard.suit, 2)

        for i, suitstring in enumerate(('club', 'Diamond', 'HEART', 'sPadE')):
            specificCard = Card(3, suitstring)
            self.assertEqual(specificCard.value, 3)
            self.assertEqual(specificCard.suit, i)

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
        self.assertFalse(Card(1, 2) <= Card(7, 0))

    def testString(self):
        assert "of" in str(Card())
        self.assertEqual("Jack of Clubs", str(Card("jack", "club")))
        self.assertEqual("4 of Diamonds", str(Card(4, "diamond")))


class DeckCase(unittest.TestCase):

    def testConstruct(self):
        pass

    def testCount(self):
        pass

    def testShuffle(self):
        pass

    def testCut(self):
        pass

    def testTopDeck(self):
        pass

    def testBottomDeck(self):
        pass

    def testDeal(self):
        pass


if __name__ == "__main__":
    unittest.main()
