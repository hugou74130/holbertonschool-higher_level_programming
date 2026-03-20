#!/usr/bin/python3
"""Module pour la classe Rectangle avec méthodes area et perimeter."""


class Rectangle:  # Définit la classe 'Rectangle'
    """Classe représentant un rectangle avec méthodes utilitaires."""

    def __init__(self, width=0, height=0):  # Constructeur
        """Initialise un Rectangle et applique la validation via setters."""
        self.width = width  # Affecte une valeur à 'self.width'
        self.height = height  # Affecte une valeur à 'self.height'

    @property
    def width(self):
        """Retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Valide et définit la largeur (doit être int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Valide et définit la hauteur (doit être int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):  # Définit la fonction 'area'
        """Calcule et retourne l'aire (width * height)."""
        return self.width * self.height

    def perimeter(self):  # Définit la fonction 'perimeter'
        """Calcule et retourne le périmètre, ou 0 si l'une des dimensions est 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
