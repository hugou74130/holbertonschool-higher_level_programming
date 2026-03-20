#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle# Affecte une valeur à 'Rectangle'

my_rectangle_1 = Rectangle(8, 4)# Affecte une valeur à 'my_rectangle_1'
my_rectangle_2 = Rectangle(2, 3)# Affecte une valeur à 'my_rectangle_2'

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):# Condition si
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")    # Affiche à l'écran
else:# Sinon
    print("my_rectangle_2 is bigger than my_rectangle_1")    # Affiche à l'écran


my_rectangle_2.width = 10# Affecte une valeur à 'my_rectangle_2.width'
my_rectangle_2.height = 5# Affecte une valeur à 'my_rectangle_2.height'
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):# Condition si
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")    # Affiche à l'écran
else:# Sinon
    print("my_rectangle_2 is bigger than my_rectangle_1")    # Affiche à l'écran
