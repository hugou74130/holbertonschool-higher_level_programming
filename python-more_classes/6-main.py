#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle# Affecte une valeur à 'Rectangle'

my_rectangle_1 = Rectangle(2, 4)# Affecte une valeur à 'my_rectangle_1'
my_rectangle_2 = Rectangle(2, 4)# Affecte une valeur à 'my_rectangle_2'
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))# Affiche à l'écran
del my_rectangle_1# Code
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))# Affiche à l'écran
del my_rectangle_2# Code
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))# Affiche à l'écran
