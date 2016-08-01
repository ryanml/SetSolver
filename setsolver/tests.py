#!/usr/bin/python
from card import Card
from solver import Solver
import unittest

class SetSolverTests(unittest.TestCase):

    """
    Tests the Card().is_equal function (Outcome: True)
    """
    def test_is_equal_equal(self):
        card_one = Card('Red', 'Solid', 'Diamond', 3)
        card_two = Card('Red', 'Solid', 'Diamond', 3)
        self.assertEqual(card_one.is_equal_to(card_two), True)

    """
    Tests the Card().is_equal function (Outcome: False)
    """
    def test_is_equal_not_equal(self):
        card_one = Card('Red', 'Solid', 'Diamond', 3)
        card_two = Card('Red', 'Solid', 'Diamond', 2)
        self.assertEqual(card_one.is_equal_to(card_two), False)

if __name__ == '__main__':
    unittest.main()
