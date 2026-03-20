#!/usr/bin/python3
"""Module rectangle avancé : symboles d'impression, comparaisons et utilitaires."""


class Rectangle:
    """Classe Rectangle fournissant plusieurs utilitaires (aire, périmètre, etc.)."""

    number_of_instances = 0  # Compteur d'instances actives
    print_symbol = "#"  # Symbole utilisé pour la représentation textuelle

    def __init__(self, width=0, height=0):
        """Initialise la largeur et la hauteur (validation via setters)."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Incrémente le compteur d'instances

    @property
    def width(self):
        """Retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Valide et assigne la largeur (doit être un int >= 0)."""
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
        """Valide et assigne la hauteur (doit être un int >= 0)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et retourne l'aire (width * height)."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcule et retourne le périmètre ou 0 si une dimension est nulle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation textuelle utilisant `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Représentation officielle pour recréer l'instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Décrémente le compteur et affiche un message à la suppression."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Retourne le rectangle avec la plus grande aire (rect_1 si égalité).

        Lève TypeError si les paramètres ne sont pas des instances de Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
