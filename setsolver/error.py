#!/usr/bin/python

class CollectionSizeError(Exception):

    # Constructor
    def __init__(self, size):
        ex_string = "Error: Collection must contain at least %d cards." % size
        super(CollectionSizeError, self).__init__(ex_string)
