#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class
and includes a method to print the list in sorted order.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or a subclass thereof.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass.
    """
    # Renvoie True si obj est instance de a_class ou d'une sous-classe
    return isinstance(obj, a_class)
