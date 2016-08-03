#!/usr/bin/python
from solver import Solver
from card import Card
from error import *

class SetSolverInterface(object):

    def __init__(self):
        self.open = True
        self.collection = []
        self.dimensions = []
        self.dimensions_set = False

    def prompt_add_card(self):
        new_card = Card()
        for dimension in self.dimensions:
            state = ""
            while len(state) == 0:
                state = raw_input("Enter value for " + dimension + ">> ")
            new_card.add_dimension(dimension, state.lower().strip())
        self.collection.append(new_card)

    def call_to_gen_set(self):
        try:
            possible_sets = self.set_solver.gen_possible_sets(self.collection)
            if possible_sets:
                print "Possible Sets:\n"
                self.set_solver.print_possible_sets(possible_sets)
            else:
                print "There are no sets that can be made."
        except CollectionSizeError:
            print "Error: There must be at least %d cards to build a set." % self.set_solver.set_size

    def prompt_for_dimensions(self):
        print "Welcome to the Set Solver\n"
        print "Enter a dimension, then hit enter."
        print "To stop adding dimensions, enter 'exit'"
        recv_dimensions = True
        while recv_dimensions:
            dimension_input = raw_input(">> ").lower().strip()
            if dimension_input == "exit":
                recv_dimensions = False
            else:
                self.dimensions.append(dimension_input)
        if len(self.dimensions) > 0:
            self.dimensions_set = True
            self.set_solver = Solver(self.dimensions)

    def prompt_for_input(self):
        self.print_menu()
        user_choice = raw_input(">> ").strip()
        if user_choice == "1":
            self.prompt_add_card()
        elif user_choice == "2":
            self.call_to_gen_set()
        elif user_choice == "3":
            print "Goodbye."
            self.open = False
        else:
            print "Invalid Input"

    def print_menu(self):
        print "\nPlease choose a number corresponding to the action you'd like to make:"
        print "1. Add a card to the collection"
        print "2. Generate all possible sets for the collection"
        print "3. Exit\n"

def main():
    interface = SetSolverInterface()
    while not interface.dimensions_set:
        interface.prompt_for_dimensions()
    while interface.open:
        interface.prompt_for_input()

if __name__ == "__main__":
    main()
