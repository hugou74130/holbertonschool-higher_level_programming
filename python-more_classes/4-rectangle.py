#!/usr/bin/python3
"""Module pour la classe Rectangle avec area, perimeter, __str__ et __repr__."""


class Rectangle:  # Définit la classe 'Rectangle'
    """Classe représentant un rectangle et ses opérations de base."""

    def __init__(self, width=0, height=0):  # Constructeur
        """Initialise largeur et hauteur via les setters (validation).

        Args:
            width (int): largeur (par défaut 0).
            height (int): hauteur (par défaut 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retourne la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Valide et définit la largeur (int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Valide et définit la hauteur (int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire (width * height)."""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre, ou 0 si une dimension est 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Représentation textuelle du rectangle en '#'."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Représentation officielle permettant de recréer l'objet."""
        return "Rectangle({}, {})".format(self.width, self.height)
