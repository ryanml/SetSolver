#!/usr/bin/python

"""
The CollectionSizeError is raised should the collection not be equal to
or exceed the requirement to create a set.
"""
class CollectionSizeError(Exception):

    # Constructor
    def __init__(self, size):
        ex_string = "Error: Collection must contain at least %d cards." % size
        super(CollectionSizeError, self).__init__(ex_string)

"""
The IncompatibleCardError is raised if a card that does the same/number of dimensions
that is demanded in a collection.
"""
class IncompatibleCardError(Exception):

    # Constructor
    def __init__(self):
        ex_string = "Error: Card is not compatible with the collection's dimensions"
        super(IncompatibleCardError, self).__init__(ex_string)
