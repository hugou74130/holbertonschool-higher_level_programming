#!/usr/bin/python3
"""
Module that defines a function to check class inheritance.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that
    inherits from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherits
        from a_class, False otherwise.
    """
    # Vérifie que l'objet est une instance d'une sous-classe de a_class
    return isinstance(obj, a_class) and type(obj) is not a_class
