#!/usr/bin/python

class Card(object):

    """
    Constructor takes in values for for dimensions:
    Color, Number, Shape, and Shading
    """
    def __init__(self):
        self.dims = {}

    """
    The add_dimension function takes in a key and value,
    and stores that as a card dimension
    """
    def add_dimension(self, dimension, state):
        self.dims[dimension] = state

    """
    The is_equal_to compares the dimensions of one
    card to another
    Params: self, card (Card object)
    Returns: boolean
    """
    def is_equal_to(self, card):
        return self.dims == card.dims
