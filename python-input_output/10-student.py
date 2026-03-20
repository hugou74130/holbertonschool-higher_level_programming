#!/usr/bin/python3
"""
This module defines the Student class.
"""


class Student:
    """Student class representing a student with simple attributes.
    Provides `to_json` which returns a dict representation.
    """
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name,
        and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance.
        If `attrs` is a list of strings, only attribute names contained in
        this list will be retrieved. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()
