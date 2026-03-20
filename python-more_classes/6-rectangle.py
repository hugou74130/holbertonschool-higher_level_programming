#!/usr/bin/python3
"""Module Rectangle avec compteur d'instances et méthodes utiles."""


class Rectangle:  # Définit la classe 'Rectangle'
    """Classe rectangle qui suit le nombre d'instances créées.

    Attributes:
        number_of_instances (int): compteur d'instances actives.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialise le rectangle et incrémente le compteur d'instances."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Incrémente le compteur

    @property
    def width(self):
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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre ou 0 si l'une des dimensions est nulle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Représentation textuelle réalisée en répétant `#` pour chaque ligne."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Représentation officielle pour recréer l'objet via eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Décrémente le compteur et affiche un message lors de la suppression."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
