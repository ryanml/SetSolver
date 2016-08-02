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
"""
class IncompatibleCardError(Exception):

    # Constructor
    def __init__(self, card):
        ex_string = "Error: %s is not compatible with the collection's dimensions" % card
        super(IncompatibleCardError, self).__init__(ex_string)
