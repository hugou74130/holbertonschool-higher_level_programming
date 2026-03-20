#!/usr/bin/python3
"""Module defining the BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class with area and integer validator methods."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        # Méthode à redéfinir par les sous-classes
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        # Vérifie que `value` est bien un int
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        # Vérifie que la valeur est strictement positive
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
