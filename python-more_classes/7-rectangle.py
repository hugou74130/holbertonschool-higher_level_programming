#!/usr/bin/python3
"""Module Rectangle avancé avec compteur d'instances et symbole d'impression."""


class Rectangle:  # Définit la classe 'Rectangle'
    """Rectangle avec attributs utilitaires et comportement standard."""

    number_of_instances = 0  # Compteur d'instances actives
    print_symbol = "#"  # Symbole utilisé pour la représentation textuelle

    def __init__(self, width=0, height=0):  # Constructeur
        """Initialise la largeur et la hauteur (validation via setters).

        Incrémente le compteur d'instances lors de la création.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Incrément du compteur

    @property
    def width(self):  # Getter de width
        """Retourne la largeur actuelle."""
        return self.__width  # Retourne le résultat

    @width.setter
    def width(self, value):  # Setter de width
        """Valide que `value` est un int >= 0 puis l'affecte."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value  # Affecte la valeur validée

    @property
    def height(self):  # Getter de height
        """Retourne la hauteur actuelle."""
        return self.__height  # Retourne le résultat

    @height.setter
    def height(self, value):  # Setter de height
        """Valide que `value` est un int >= 0 puis l'affecte."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value  # Affecte la valeur validée

    def area(self):  # Définit la fonction 'area'
        """Calcule et retourne l'aire (width * height)."""
        return self.__width * self.__height  # Retourne le résultat

    def perimeter(self):  # Définit la fonction 'perimeter'
        """Calcule et retourne le périmètre, ou 0 si une dimension est nulle."""
        if self.__width == 0 or self.__height == 0:
            return 0  # Retourne le résultat
        return 2 * (self.__width + self.__height)  # Retourne le résultat

    def __str__(self):  # Définit la fonction '__str__'
        """Retourne la représentation en utilisant `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""  # Retourne une chaîne vide si l'une des dimensions est 0
        symbol = str(self.print_symbol)  # Récupère le symbole d'affichage
        return "\n".join([symbol * self.__width for _ in range(self.__height)])  # Retourne le résultat

    def __repr__(self):  # Définit la fonction '__repr__'
        """Retourne une chaîne officielle permettant de recréer l'objet."""
        return f"Rectangle({self.__width}, {self.__height})"  # Retourne le résultat

    def __del__(self):  # Définit la fonction '__del__'
        """Décrémente le compteur et affiche un message à la suppression."""
        Rectangle.number_of_instances -= 1  # Décrémente le compteur
        print("Bye rectangle...")  # Affiche à l'écran