#!/usr/bin/python3
"""
This module contains the function class_to_json
that returns the dictionary description with simple data structure
for JSON serialization of an object:
"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure for JSON
    serialization of an object.
    Parameters
    ----------
    obj : object
        The object to convert to a dictionary for JSON serialization.
    Returns
    -------
    dict
        A dictionary containing the key-value pairs of `obj`'s attributes,
        where keys are attribute names and
        values are their corresponding values.
    Notes
    -----
    - Only includes attributes that are of simple data types (e.g., str, int,
      list, dict).
    - Does not include methods or attributes that are not JSON serializable.
    - Uses `obj.__dict__` to access the object's attributes.
    - If `obj` has attributes that are not JSON serializable, they will be
      included in the dictionary but may cause issues when attempting to
      serialize to JSON.
    """
    return obj.__dict__
