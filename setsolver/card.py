#!/usr/bin/python

class Card(object):

    """
    Constructor takes in values for for dimensions:
    Color, Number, Shape, and Shading
    """
    def __init__(self, color, number, shape, shading):
        self.dims = {}
        self.dims['color'] = color
        self.dims['number'] = number
        self.dims['shape'] = shape
        self.dims['shading'] = shading

    """
    The is_equal_to compares the dimensions of one
    card to another
    Params: self, card (Card object)
    Returns: boolean
    """
    def is_equal_to(self, card):
        return self.dims == card.dims
