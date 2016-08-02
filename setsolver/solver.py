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
    combinations of cards given a collection of them
    Params: collection (list of Card objects)
    Returns: perms (list of lists of Card objects)
    """
    def gen_possible_sets(self, collection):
        if len(collection) < self.set_size:
            raise CollectionSizeError(self.set_size)
