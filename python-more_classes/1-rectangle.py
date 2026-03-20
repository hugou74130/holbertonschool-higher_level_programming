#!/usr/bin/python3
"""Module pour la classe Rectangle.

Ce module définit une classe simple `Rectangle` avec des propriétés
`width` et `height` incluant la validation des valeurs.
"""


class Rectangle:  # Définition de la classe 'Rectangle'
    """Classe représentant un rectangle avec largeur et hauteur privées.

    Attributes:
        __width (int): largeur du rectangle (privée, >= 0).
        __height (int): hauteur du rectangle (privée, >= 0).
    """

    def __init__(self, width=0, height=0):  # Constructeur
        """Initialise un nouveau Rectangle.

        Args:
            width (int, optional): largeur. Défaut 0.
            height (int, optional): hauteur. Défaut 0.
        """
        # Utilise les setters pour appliquer la validation
        self.width = width  # Affecte une valeur à 'self.width'
        self.height = height  # Affecte une valeur à 'self.height'

    @property
    def width(self):  # Getter pour width
        """Retourne la largeur actuelle."""
        return self.__width  # Retourne le résultat

    @width.setter
    def width(self, value):  # Setter pour width
        """Valide et définit la largeur.

        Lève TypeError si `value` n'est pas un int, ValueError si < 0.
        """
        if not isinstance(value, int):  # Vérifie le type
            raise TypeError("width must be an integer")
        if value < 0:  # Vérifie la valeur
            raise ValueError("width must be >= 0")
        self.__width = value  # Affecte la valeur validée

    @property
    def height(self):  # Getter pour height
        """Retourne la hauteur actuelle."""
        return self.__height  # Retourne le résultat

    @height.setter
    def height(self, value):  # Setter pour height
        """Valide et définit la hauteur.

        Lève TypeError si `value` n'est pas un int, ValueError si < 0.
        """
        if not isinstance(value, int):  # Vérifie le type
            raise TypeError("height must be an integer")
        if value < 0:  # Vérifie la valeur
            raise ValueError("height must be >= 0")
        self.__height = value  # Affecte la valeur validée
