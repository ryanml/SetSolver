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
        card_one = Card()
        card_one.add_dimension('Color', 'Red')
        card_one.add_dimension('Shading', 'Solid')
        card_one.add_dimension('Shape', 'Diamond')
        card_one.add_dimension('Number', 3)
        card_two = Card()
        card_two.add_dimension('Color', 'Red')
        card_two.add_dimension('Shading', 'Solid')
        card_two.add_dimension('Shape', 'Diamond')
        card_two.add_dimension('Number', 3)
        self.assertEqual(card_one.is_equal_to(card_two), True)

    """
    Tests the Card().is_equal function (Outcome: False)
    """
    def test_is_equal_not_equal(self):
        card_one = Card()
        card_one.add_dimension('Color', 'Red')
        card_one.add_dimension('Shading', 'Solid')
        card_one.add_dimension('Shape', 'Diamond')
        card_one.add_dimension('Number', 3)
        card_two = Card()
        card_two.add_dimension('Color', 'Red')
        card_two.add_dimension('Shading', 'Solid')
        card_two.add_dimension('Shape', 'Diamond')
        card_two.add_dimension('Number', 2)
        self.assertEqual(card_one.is_equal_to(card_two), False)

    """
    Tests that the proper exception is raised when there are too few cards
    in a given collection.
    """
    def test_card_set_too_small(self):
        set_solver = Solver(['Color', 'Shading', 'Shape', 'Number'])
        card_one = Card()
        card_one.add_dimension('Color', 'Red')
        card_one.add_dimension('Shading', 'Solid')
        card_one.add_dimension('Shape', 'Diamond')
        card_one.add_dimension('Number', 3)
        card_two = Card()
        card_two.add_dimension('Color', 'Red')
        card_two.add_dimension('Shading', 'Solid')
        card_two.add_dimension('Shape', 'Diamond')
        card_two.add_dimension('Number', 2)
        collection = [card_one, card_two]
        self.assertRaises(CollectionSizeError, set_solver.gen_possible_sets, collection)

    """
    Tests that a card with too few dimensions throws the IncompatibleCardError
    """
    def test_incompatible_card_too_few_dimensions(self):
        set_solver = Solver(['Color', 'Shading', 'Shape', 'Number'])
        card_one = Card()
        card_one.add_dimension('Color', 'Red')
        card_one.add_dimension('Shading', 'Solid')
        card_one.add_dimension('Shape', 'Diamond')
        card_one.add_dimension('Number', 3)
        card_two = Card()
        card_two.add_dimension('Color', 'Green')
        card_two.add_dimension('Shading', 'Striped')
        card_two.add_dimension('Shape', 'Squiggle')
        card_two.add_dimension('Number', 2)
        card_three = Card()
        # Card three is missing the shape dimensions
        card_three.add_dimension('Color', 'Purple')
        card_three.add_dimension('Shading', 'Empty')
        card_three.add_dimension('Number', 1)
        collection = [card_one, card_two, card_three]
        self.assertRaises(IncompatibleCardError, set_solver.gen_possible_sets, collection)

    """
    Tests that three cards differing in every single dimension is considered a set
    """
    def test_is_a_set_all_not_equal(self):
        set_solver = Solver(['Color', 'Shading', 'Shape', 'Number'])
        card_one = Card()
        card_one.add_dimension('Color', 'Red')
        card_one.add_dimension('Shading', 'Solid')
        card_one.add_dimension('Shape', 'Diamond')
        card_one.add_dimension('Number', 3)
        card_two = Card()
        card_two.add_dimension('Color', 'Green')
        card_two.add_dimension('Shading', 'Striped')
        card_two.add_dimension('Shape', 'Squiggle')
        card_two.add_dimension('Number', 2)
        card_three = Card()
        card_three.add_dimension('Color', 'Purple')
        card_three.add_dimension('Shading', 'Empty')
        card_three.add_dimension('Shape', 'Oval')
        card_three.add_dimension('Number', 1)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), True)

    """
    Tests that two of three cards that are the same return False (not a set)
    """
    def test_is_a_set_two_equal_cards(self):
        set_solver = Solver(['Color', 'Shading', 'Shape', 'Number'])
        card_one = Card()
        card_one.add_dimension('Color', 'Red')
        card_one.add_dimension('Shading', 'Solid')
        card_one.add_dimension('Shape', 'Diamond')
        card_one.add_dimension('Number', 3)
        card_two = Card()
        card_two.add_dimension('Color', 'Green')
        card_two.add_dimension('Shading', 'Striped')
        card_two.add_dimension('Shape', 'Squiggle')
        card_two.add_dimension('Number', 2)
        card_three = Card()
        card_three.add_dimension('Color', 'Red')
        card_three.add_dimension('Shading', 'Solid')
        card_three.add_dimension('Shape', 'Diamond')
        card_three.add_dimension('Number', 3)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), False)

    """
    Tests that a true set is indeed considered a set
    """
    def test_is_a_set_qualifying_cards(self):
        set_solver = Solver(['Color', 'Shading', 'Shape', 'Number'])
        card_one = Card()
        card_one.add_dimension('Color', 'Purple')
        card_one.add_dimension('Shading', 'Empty')
        card_one.add_dimension('Shape', 'Squiggle')
        card_one.add_dimension('Number', 2)
        card_two = Card()
        card_two.add_dimension('Color', 'Purple')
        card_two.add_dimension('Shading', 'Empty')
        card_two.add_dimension('Shape', 'Oval')
        card_two.add_dimension('Number', 1)
        card_three = Card()
        card_three.add_dimension('Color', 'Purple')
        card_three.add_dimension('Shading', 'Empty')
        card_three.add_dimension('Shape', 'Diamond')
        card_three.add_dimension('Number', 3)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), True)

    """
    Tests that a true set is indeed considered a set
    """
    def test_is_a_set_more_qualifying_cards(self):
        set_solver = Solver(['Color', 'Shading', 'Shape', 'Number'])
        card_one = Card()
        card_one.add_dimension('Color', 'Purple')
        card_one.add_dimension('Shading', 'Empty')
        card_one.add_dimension('Shape', 'Oval')
        card_one.add_dimension('Number', 1)
        card_two = Card()
        card_two.add_dimension('Color', 'Green')
        card_two.add_dimension('Shading', 'Empty')
        card_two.add_dimension('Shape', 'Squiggle')
        card_two.add_dimension('Number', 1)
        card_three = Card()
        card_three.add_dimension('Color', 'Red')
        card_three.add_dimension('Shading', 'Empty')
        card_three.add_dimension('Shape', 'Diamond')
        card_three.add_dimension('Number', 1)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), True)

    """
    Tests that a false set is not considered a set
    """
    def test_is_a_set_no_qualifying_cards(self):
        set_solver = Solver(['Color', 'Shading', 'Shape', 'Number'])
        card_one = Card()
        card_one.add_dimension('Color', 'Purple')
        card_one.add_dimension('Shading', 'Striped')
        card_one.add_dimension('Shape', 'Squiggle')
        card_one.add_dimension('Number', 1)
        card_two = Card()
        card_two.add_dimension('Color', 'Green')
        card_two.add_dimension('Shading', 'Solid')
        card_two.add_dimension('Shape', 'Squiggle')
        card_two.add_dimension('Number', 2)
        card_three = Card()
        card_three.add_dimension('Color', 'Green')
        card_three.add_dimension('Shading', 'Striped')
        card_three.add_dimension('Shape', 'Diamond')
        card_three.add_dimension('Number', 1)
        collection = [card_one, card_two, card_three]
        self.assertEqual(set_solver.is_a_set(collection), False)

    """
    Tests gen_possible_sets for 12 cards
    (Taken from http://www.setgame.com/set/puzzle, solves the August 2nd, 2016 challenge)
    """
    def test_gen_possible_sets_twelve_cards(self):
        set_solver = Solver(['Color', 'Shading', 'Shape', 'Number'])
        card_one = Card()
        card_one.add_dimension('Color', 'Green')
        card_one.add_dimension('Shading', 'Solid')
        card_one.add_dimension('Shape', 'Squiggle')
        card_one.add_dimension('Number', 1)
        card_two = Card()
        card_two.add_dimension('Color', 'Purple')
        card_two.add_dimension('Shading', 'Empty')
        card_two.add_dimension('Shape', 'Diamond')
        card_two.add_dimension('Number', 2)
        card_three = Card()
        card_three.add_dimension('Color', 'Purple')
        card_three.add_dimension('Shading', 'Striped')
        card_three.add_dimension('Shape', 'Squiggle')
        card_three.add_dimension('Number', 1)
        card_four = Card()
        card_four.add_dimension('Color', 'Purple')
        card_four.add_dimension('Shading', 'Striped')
        card_four.add_dimension('Shape', 'Oval')
        card_four.add_dimension('Number', 1)
        card_five = Card()
        card_five.add_dimension('Color', 'Red')
        card_five.add_dimension('Shading', 'Striped')
        card_five.add_dimension('Shape', 'Oval')
        card_five.add_dimension('Number', 1)
        card_six = Card()
        card_six.add_dimension('Color', 'Red')
        card_six.add_dimension('Shading', 'Striped')
        card_six.add_dimension('Shape', 'Oval')
        card_six.add_dimension('Number', 2)
        card_seven = Card()
        card_seven.add_dimension('Color', 'Green')
        card_seven.add_dimension('Shading', 'Solid')
        card_seven.add_dimension('Shape', 'Squiggle')
        card_seven.add_dimension('Number', 2)
        card_eight = Card()
        card_eight.add_dimension('Color', 'Green')
        card_eight.add_dimension('Shading', 'Striped')
        card_eight.add_dimension('Shape', 'Diamond')
        card_eight.add_dimension('Number', 3)
        card_nine = Card()
        card_nine.add_dimension('Color', 'Purple')
        card_nine.add_dimension('Shading', 'Empty')
        card_nine.add_dimension('Shape', 'Squiggle')
        card_nine.add_dimension('Number', 1)
        card_ten = Card()
        card_ten.add_dimension('Color', 'Purple')
        card_ten.add_dimension('Shading', 'Solid')
        card_ten.add_dimension('Shape', 'Squiggle')
        card_ten.add_dimension('Number', 3)
        card_eleven = Card()
        card_eleven.add_dimension('Color', 'Red')
        card_eleven.add_dimension('Shading', 'Striped')
        card_eleven.add_dimension('Shape', 'Oval')
        card_eleven.add_dimension('Number', 3)
        card_twelve = Card()
        card_twelve.add_dimension('Color', 'Green')
        card_twelve.add_dimension('Shading', 'Striped')
        card_twelve.add_dimension('Shape', 'Diamond')
        card_twelve.add_dimension('Number', 1)
        collection = [card_one, card_two, card_three, card_four,
                      card_five, card_six, card_seven, card_eight,
                      card_nine, card_ten, card_eleven, card_twelve]
        # Placed as members of one list for the test, each set is each group of three cards
        correct_sets = [{'Color': 'Green', 'Shading': 'Solid', 'Shape': 'Squiggle', 'Number': 1},
                        {'Color': 'Purple', 'Shading': 'Empty', 'Shape': 'Diamond', 'Number': 2},
                        {'Color': 'Red', 'Shading': 'Striped', 'Shape': 'Oval', 'Number': 3},
                        {'Color': 'Purple', 'Shading': 'Empty', 'Shape': 'Diamond', 'Number': 2},
                        {'Color': 'Purple', 'Shading': 'Striped', 'Shape': 'Oval', 'Number': 1},
                        {'Color': 'Purple', 'Shading': 'Solid', 'Shape': 'Squiggle', 'Number': 3},
                        {'Color': 'Purple', 'Shading': 'Empty', 'Shape': 'Diamond', 'Number': 2},
                        {'Color': 'Red', 'Shading': 'Striped', 'Shape': 'Oval', 'Number': 2},
                        {'Color': 'Green', 'Shading': 'Solid', 'Shape': 'Squiggle', 'Number': 2},
                        {'Color': 'Purple', 'Shading': 'Striped', 'Shape': 'Squiggle', 'Number': 1},
                        {'Color': 'Red', 'Shading': 'Striped', 'Shape': 'Oval', 'Number': 1},
                        {'Color': 'Green', 'Shading': 'Striped', 'Shape': 'Diamond', 'Number': 1},
                        {'Color': 'Purple', 'Shading': 'Striped', 'Shape': 'Squiggle', 'Number': 1},
                        {'Color': 'Red', 'Shading': 'Striped', 'Shape': 'Oval', 'Number': 2},
                        {'Color': 'Green', 'Shading': 'Striped', 'Shape': 'Diamond', 'Number': 3},
                        {'Color': 'Red', 'Shading': 'Striped', 'Shape': 'Oval', 'Number': 1},
                        {'Color': 'Red', 'Shading': 'Striped', 'Shape': 'Oval', 'Number': 2},
                        {'Color': 'Red', 'Shading': 'Striped', 'Shape': 'Oval', 'Number': 3}]
        possible_sets = set_solver.gen_possible_sets(collection)
        # Compares each card in the possible_sets to the confirmed cards of the correct set
        card_inc = 0
        for card_set in possible_sets:
            for card in card_set:
                self.assertEqual(card.dims, correct_sets[card_inc])
                card_inc += 1

if __name__ == '__main__':
    unittest.main()
