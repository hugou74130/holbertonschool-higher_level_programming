#!/usr/bin/python3
"""
This module contains the function save_to_json_file
that writes an Object to a text file, using a JSON representation:
"""


import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file using JSON representation.
    Parameters
    ----------
    my_obj : object
        The Python object to serialize to JSON
        (for example, a dict or list).
    filename : str
        Path to the file where the JSON representation
        will be written. The file
        is created if it does not exist and overwritten
        if it does.
    Returns
    -------
    None
    Raises
    ------
    TypeError
        If `my_obj` contains objects that are not JSON serializable.
    OSError
        If the file cannot be opened or written to.
    Notes
    -----
    - Uses `json.dump` to write the JSON representation and opens the file with
      UTF-8 encoding.
    - Uses the `with` statement to ensure the file is properly closed.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
