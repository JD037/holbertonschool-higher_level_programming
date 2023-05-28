#!/usr/bin/python3
#create MyList class that inheirits from list
"""This module contains the class MyList."""


class MyList(list):
    """Class MyList that inherits from list."""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
