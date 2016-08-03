#!/usr/bin/python
from solver import Solver
from card import Card
from error import *

class SetSolverInterface(object):

    """
    Constructor sets four needed attributes to their defaults.
    """
    def __init__(self):
        # Open defines whether or not we continue with the program
        self.open = True
        # Collection will be the list of card objects
        self.collection = []
        # Dimensions will be the allowed dimensions for the card collection
        self.dimensions = []
        # Dimensions are set by the user, so they are false initially
        self.dimensions_set = False

    """
    The prompt_add_card function prompts the user to set the state
    for each dimension to add a new card.
    """
    def prompt_add_card(self):
        new_card = Card()
        for dimension in self.dimensions:
            state = ""
            while len(state) == 0:
                state = raw_input("Enter value for " + dimension + ">> ")
            # Adds state at dimension for the new card
            new_card.add_dimension(dimension, state.lower().strip())
        # Add the new card to the colleciton
        self.collection.append(new_card)

    """
    The call_to_gen_set function attempts to get all of the possible sets
    for the card collection
    """
    def call_to_gen_set(self):
        try:
            # Get all of the possible sets
            possible_sets = self.set_solver.gen_possible_sets(self.collection)
            # If there were possible sets, print them out
            if possible_sets:
                print "Possible Sets:\n"
                self.set_solver.print_possible_sets(possible_sets)
            # If not, let the user know
            else:
                print "There are no sets that can be made."
        # If there were not enough cards to make a set, let the user know
        except CollectionSizeError:
            print "Error: There must be at least %d cards to build a set." % self.set_solver.set_size

    """
    The delete_last_card function attempts to delete the last card entered
    if it exists.
    """
    def delete_last_card(self):
        if len(self.collection) == 0:
            print "Error: There are no cards in the collection."
        else:
            deleted_card = self.collection.pop()
            print "Card with following dimensions deleted:\n", deleted_card.dims

    """
    The prompt_for_dimensions function gets the dimensions from the user that will persist
    for the card collection.
    """
    def prompt_for_dimensions(self):
        print "Welcome to the Set Solver\n"
        print "Enter a dimension, then hit enter."
        print "To stop adding dimensions, enter 'exit'"
        recv_dimensions = True
        # Dimensions are put in by the user until they enter 'exit'
        while recv_dimensions:
            dimension_input = raw_input(">> ").lower().strip()
            if dimension_input == "exit":
                recv_dimensions = False
            else:
                self.dimensions.append(dimension_input)
        # If we have added at least one dimension, the dimensions are set
        if len(self.dimensions) > 0:
            self.dimensions_set = True
            # Create a new solver object with the dimensions
            self.set_solver = Solver(self.dimensions)

    """
    The prompt_for_input function is called while the program is open. It calls the
    appropriate function for given input.
    """
    def prompt_for_input(self):
        self.print_menu()
        user_choice = raw_input(">> ").strip()
        if user_choice == "1":
            self.prompt_add_card()
        elif user_choice == "2":
            self.call_to_gen_set()
        elif user_choice == "3":
            self.delete_last_card()
        elif user_choice == "4":
            print "Goodbye."
            self.open = False
        else:
            print "Invalid Input"

    """
    The print_menu function prints the menu of options.
    """
    def print_menu(self):
        print "\nPlease choose a number corresponding to the action you'd like to make:"
        print "1. Add a card to the collection"
        print "2. Generate all possible sets for the collection"
        print "3. Delete the last card entered."
        print "4. Exit\n"

def main():
    interface = SetSolverInterface()
    while not interface.dimensions_set:
        interface.prompt_for_dimensions()
    while interface.open:
        interface.prompt_for_input()

if __name__ == "__main__":
    main()
