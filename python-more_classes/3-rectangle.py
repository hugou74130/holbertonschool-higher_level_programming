#!/usr/bin/python3
"""Module définissant une classe Rectangle avec méthodes utilitaires."""


class Rectangle:  # Définit la classe 'Rectangle'
    """Classe qui définit un rectangle avec largeur et hauteur privées."""

    def __init__(self, width=0, height=0):  # Constructeur
        """Initialise un nouveau Rectangle.

        Args:
            width (int): largeur (par défaut 0).
            height (int): hauteur (par défaut 0).
        """
        self.width = width  # Affecte une valeur à 'self.width'
        self.height = height  # Affecte une valeur à 'self.height'

    @property
    def width(self):  # Getter width
        """Retourne la largeur actuelle."""
        return self.__width  # Retourne le résultat

    @width.setter
    def width(self, value):  # Setter width
        """Valide et définit la largeur (int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):  # Getter height
        """Retourne la hauteur actuelle."""
        return self.__height  # Retourne le résultat

    @height.setter
    def height(self, value):  # Setter height
        """Valide et définit la hauteur (int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):  # Définit la fonction 'area'
        """Calcule et retourne l'aire (width * height)."""
        return self.__width * self.__height  # Retourne le résultat

    def perimeter(self):  # Définit la fonction 'perimeter'
        """Calcule et retourne le périmètre, ou 0 si une dimension est 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):  # Définit la fonction '__str__'
        """Retourne une représentation textuelle du rectangle avec '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        # Construit la liste de lignes puis rejoint avec des sauts de ligne
        rectangle_str = []
        for _ in range(self.__height):  # Pour chaque ligne
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)  # Retourne le résultat