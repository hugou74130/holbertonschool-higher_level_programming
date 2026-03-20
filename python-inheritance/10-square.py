#!/usr/bin/python3
"""Module defining the Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with size.

        Args:
            size: The size of the square (must be a positive integer)
        """
        # Vérifie que `size` est un entier strictement positif
        self.integer_validator("size", size)
        # Crée un rectangle de taille (size, size) pour représenter le carré
        super().__init__(size, size)
