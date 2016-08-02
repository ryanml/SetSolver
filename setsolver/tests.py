#!/usr/bin/python
from card import Card
from solver import Solver
from error import *
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

    """
    Tests that the proper exception is raised when there are too few cards
    in a given collection.
    """
    def test_card_set_too_small(self):
        set_solver = Solver()
        card_one = Card('Red', 'Solid', 'Diamond', 3)
        card_two = Card('Red', 'Solid', 'Diamond', 2)
        collection = [card_one, card_two]
        self.assertRaises(CollectionSizeError, set_solver.gen_possible_sets, collection)

    """
    Tests that three cards differing in every single dimension is considered a set
    """
    def test_is_a_set_all_not_equal(self):
        set_solver = Solver()
        card_one = Card('Red', 'Solid', 'Diamond', 3)
        card_two = Card('Green', 'Striped', 'Squiggle', 2)
        card_three = Card('Purple', 'Empty', 'Oval', 1)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), True)

    """
    Tests that two of three cards that are the same return False (not a set)
    """
    def test_is_a_set_two_equal_cards(self):
        set_solver = Solver()
        card_one = Card('Red', 'Solid', 'Diamond', 3)
        card_two = Card('Green', 'Striped', 'Squiggle', 2)
        card_three = Card('Red', 'Solid', 'Diamond', 3)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), False)

    """
    Tests that a true set is indeed considered a set
    """
    def test_is_a_set_qualifying_cards(self):
        set_solver = Solver()
        card_one = Card('Purple', 'Empty', 'Squiggle', 2)
        card_two = Card('Purple', 'Empty', 'Oval', 1)
        card_three = Card('Purple', 'Empty', 'Diamond', 3)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), True)

    """
    Tests that a true set is indeed considered a set
    """
    def test_is_a_set_more_qualifying_cards(self):
        set_solver = Solver()
        card_one = Card('Purple', 'Empty', 'Oval', 1)
        card_two = Card('Green', 'Empty', 'Squiggle', 1)
        card_three = Card('Red', 'Empty', 'Diamond', 1)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), True)

    """
    Tests that a false set is not considered a set
    """
    def test_is_a_set_no_qualifying_cards(self):
        set_solver = Solver()
        card_one = Card('Purple', 'Striped', 'Squiggle', 1)
        card_two = Card('Green', 'Solid', 'Squiggle', 2)
        card_three = Card('Green', 'Striped', 'Diamond', 1)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), False)

if __name__ == '__main__':
    unittest.main()
