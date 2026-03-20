#!/usr/bin/python3
"""Module defining the Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Args:
            width: The width of the rectangle (must be a positive integer)
            height: The height of the rectangle (must be a positive integer)
        """
        # Utilise le validator pour s'assurer que width et height sont valides
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Stocke les attributs privés
        self.__width = width
        self.__height = height
