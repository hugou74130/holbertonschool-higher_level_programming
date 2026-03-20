#!/usr/bin/python3
"""
This module contains the function from_json_string
that returns an object (Python data structure) represented by a JSON string:
"""


import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Parameters
    ----------
    my_str : str
        JSON formatted string to deserialize.

    Returns
    -------
    object
        Python representation of the JSON string (e.g., dict, list).

    Raises
    ------
    TypeError
        If `my_str` is not a string.
    json.JSONDecodeError
        If `my_str` is not a valid JSON document.
    """
    return json.loads(my_str)
