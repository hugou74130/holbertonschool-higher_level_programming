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
        # Valide que `size` est un entier positif via le validator hérité
        self.integer_validator("size", size)
        # Initialise la classe Rectangle en fournissant largeur=hauteur=size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        # Utilise les attributs privés de Rectangle pour former la chaîne
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height
        )
