#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle# Affecte une valeur à 'Rectangle'

my_rectangle = Rectangle(2, 4)# Affecte une valeur à 'my_rectangle'
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))# Affiche à l'écran

del my_rectangle# Code

try:# Bloc try
    print(my_rectangle)    # Affiche à l'écran
except Exception as e:# Capture l'exception
    print("[{}] {}".format(e.__class__.__name__, e))    # Affiche à l'écran
