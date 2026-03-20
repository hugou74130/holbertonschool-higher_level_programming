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
        # Validation des paramètres via la méthode héritée
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Stocke les valeurs privées de largeur et hauteur
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        # Aire = largeur * hauteur
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        # Représentation lisible du rectangle
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
