#!/usr/bin/python3
"""Module Rectangle avec méthodes d'utilité et destructeur."""


class Rectangle:  # Définit la classe 'Rectangle'
    """Classe rectangle avec area, perimeter et représentation textuelle."""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle en utilisant les setters (validation)."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retourne la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calcule le périmètre si les dimensions sont non nulles, sinon retourne 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Retourne une représentation en lignes composées de '#'."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Retourne la représentation officielle utilisable avec eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Message affiché lors de la suppression d'une instance."""
        print("Bye rectangle...")
