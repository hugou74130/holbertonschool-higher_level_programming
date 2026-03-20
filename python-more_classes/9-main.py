#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle# Affecte une valeur à 'Rectangle'

my_square = Rectangle.square(5)# Affecte une valeur à 'my_square'
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))# Affiche à l'écran
print(my_square)# Affiche à l'écran
