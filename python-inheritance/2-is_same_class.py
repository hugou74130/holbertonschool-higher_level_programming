#!/usr/bin/python3
"""Module that checks if object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class."""
    # Utilise `type(obj) is a_class` pour vérifier l'instance exacte de l'objet 
    return type(obj) is a_class
