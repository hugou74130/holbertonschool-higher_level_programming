#!/usr/bin/python3
"""This module defines a class MyList."""
# permet de dafficher une liste triée sans modifier l'original 

class MyList(list):
    """A class that inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))