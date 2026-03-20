#!/usr/bin/python3
"""
This module contains the function to_json_string
that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    Args:
        my_obj: The object to serialize to JSON
    Returns:
        str: JSON string representation of my_obj
    """
    return json.dumps(my_obj)
