#!/usr/bin/python
from error import *

class Solver(object):
    """
    Constructor takes in a set size argument
    """
    def __init__(self, set_size=3):
        self.set_size = set_size

    """
    The gen_possible_sets function generates all possible
    sets of cards given a collection of them
    Params: collection (list of Card objects)
    Returns: perms (list of lists of Card objects)
    """
    def gen_possible_sets(self, collection):
        if len(collection) < self.set_size:
            raise CollectionSizeError(self.set_size)
            
    """
    The is_a_set function takes in a list of three card objects
    and determines if it qualifies as a set_size
    """
    def is_a_set(self, cards):
        card_one = cards[0]
        card_two = cards[1]
        card_three = cards[2]
        f_set = set(card_one.dims.items())
        s_set = set(card_two.dims.items())
        t_set = set(card_three.dims.items())
        comps = [f_set & s_set, f_set & t_set, s_set & t_set]
        # If all cards have ntirely different dimensions, it is a set
        for comp in comps:
            if len(comp) != 0:
                return False
        return True
