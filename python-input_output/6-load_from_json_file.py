#!/usr/bin/python3
"""
This module contains the function load_from_json_file
that creates an Object from a “JSON file”:
"""


import json


def load_from_json_file(filename):
    """Create an object from a JSON file and return it.

    Parameters
    ----------
    filename : str
        Path to the JSON file to read.

    Returns
    -------
    object
        The Python object represented by the JSON content (for example, a
        dict or list).

    Raises
    ------
    FileNotFoundError
        If `filename` does not exist.
    json.JSONDecodeError
        If the file does not contain valid JSON.
    OSError
        If the file cannot be opened or read.

    Notes
    -----
    - The file is opened with UTF-8 encoding.
    - Uses `json.load` to deserialize the file content.
    - Uses the `with` statement so the file is closed automatically.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
