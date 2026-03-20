#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle# Affecte une valeur à 'Rectangle'

my_rectangle = Rectangle(2, 4)# Affecte une valeur à 'my_rectangle'
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))# Affiche à l'écran

print("--")# Affiche à l'écran

my_rectangle.width = 10# Affecte une valeur à 'my_rectangle.width'
my_rectangle.height = 3# Affecte une valeur à 'my_rectangle.height'
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))# Affiche à l'écran
