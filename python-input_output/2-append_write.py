#!/usr/bin/python3
"""This module contains the function append_write that appends a string
to a text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns the number
    of characters added.

    Args:
        filename: name of the file to append to
        text: string to append to the file

    Returns:
        Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
