#!/usr/bin/python3
"""
This module contains the function class_to_json
that returns the dictionary description with simple data structure
for JSON serialization of an object:
"""


class Student:
    """Student class representing a student with simple attributes.

    Provides `to_json` which returns a dict representation.
    """
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last
        name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of the Student instance."""
        return self.__dict__
