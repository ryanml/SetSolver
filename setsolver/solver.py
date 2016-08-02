#!/usr/bin/python
import itertools
from error import *

class Solver(object):
    """
    Constructor takes in a set size argument
    """
    def __init__(self, set_size=3, num_dimensions=4):
        self.set_size = set_size
        self.num_dimensions = num_dimensions

    """
    The gen_possible_sets function generates all possible
    sets of cards given a collection of them
    Params: collection (list of Card objects)
    Returns: perms (list of lists of Card objects), False if no sets are found
    """
    def gen_possible_sets(self, collection):
        # Check to make sure the collection length
        # is large enough to generate a set
        coll_len = len(collection)
        if coll_len < self.set_size:
            raise CollectionSizeError(self.set_size)
        # Set possible sets to an empty list
        possible_sets = []
        # Generate all combinations of cards
        combinations = list(itertools.combinations(collection, self.set_size))
        # Check if each combination is a set, if it is, push it to possible_sets list
        for comb in combinations:
            if self.is_a_set(comb):
                possible_sets.append(comb)
        # If there are no possible sets, return False, else return the sets
        if len(possible_sets) == 0:
            return False
        else:
            return possible_sets

    """
    The is_a_set function takes in a list of three card objects
    and determines if it qualifies as a set
    """
    def is_a_set(self, cards):
        dims_in_common = []
        cards_all_qualify = True
        cards_too_similar = False
        cards_all_different = True
        # Create a set type from the dimensions dict for each card
        f_set = set(cards[0].dims.items())
        s_set = set(cards[1].dims.items())
        t_set = set(cards[2].dims.items())
        # Compare each card, using & to get similarities between them
        comps = [f_set & s_set, f_set & t_set, s_set & t_set]
        # Iterate through the comparisons
        for comp in comps:
            # The cards will not be all different if there are any similarities
            if len(comp) != 0:
                cards_all_different = False
            # If two of the cards are equal, they are too similar to be a set
            if len(comp) == self.num_dimensions:
                cards_too_similar = True
            # If neither above condition is met, pust similarities to list
            else:
                dims_in_common.append(list(comp))
        if len(dims_in_common) > 0:
            # Use the first set of common dimensions for a comparison
            first_common_dim = dims_in_common[0]
            # Loop through the similarities
            for d in range(0, len(dims_in_common)):
                # If they all don't have the same similarities, the cards do not qualify
                if dims_in_common[d] != first_common_dim:
                    cards_all_qualify = False
        # If the cards are all different, or they aren't too similar and they qualify, return True
        if cards_all_different or (not cards_too_similar and cards_all_qualify):
            return True
        else:
            return False

    """
    The print_possible_sets function prints and formats all of the given
    sets in a readable format.
    """
    def print_possible_sets(self, sets):
        pass
        
