import unittest
from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Clubs", 5)
        self.card3 = Card("Hearts", 10)
        self.card4 = Card("Spades", 9)
        self.card5 = Card("Clubs", 8)
    
        self.cardhand1 = [self.card1,self.card2,self.card3]
        self.cardhand2 =[self.card3,self.card4,self.card5]

    def test_has_ace(self):
        card1_value = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(True, card1_value)

    def test_has_no_ace(self):
        card2_value = CardGame.check_for_ace(self, self.card2)
        self.assertEqual(False, card2_value)

    def test_card1_greater(self):
        winner = CardGame.highest_card(self, self.card3, self.card2)
        self.assertEqual(self.card3, winner)

    def test_card2_greater(self):
        winner = CardGame.highest_card(self, self.card1,self.card2)
        self.assertEqual(self.card2, winner)


    def test_total_cardhand1(self):
        result = CardGame.cards_total(self, self.cardhand1)
        self.assertEqual("You have a total of 16", result)

    def test_total_cardhand2(self):
        result = CardGame.cards_total(self, self.cardhand2)
        self.assertEqual("You have a total of 27", result)