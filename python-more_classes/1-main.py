#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle# Affecte une valeur à 'Rectangle'

my_rectangle = Rectangle(2, 4)# Affecte une valeur à 'my_rectangle'
print(my_rectangle.__dict__)# Affiche à l'écran

my_rectangle.width = 10# Affecte une valeur à 'my_rectangle.width'
my_rectangle.height = 3# Affecte une valeur à 'my_rectangle.height'
print(my_rectangle.__dict__)# Affiche à l'écran
