#!/usr/bin/python3
"""Module that defines the lookup function."""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing attributes and methods.
    """
    # Utilise la fonction intégrée `dir()` pour obtenir tous les attributs
    # et méthodes accessibles sur l'objet (liste de chaînes).
    return dir(obj)
