#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle# Affecte une valeur à 'Rectangle'

my_rectangle_1 = Rectangle(8, 4)# Affecte une valeur à 'my_rectangle_1'
print(my_rectangle_1)# Affiche à l'écran
print("--")# Affiche à l'écran
my_rectangle_1.print_symbol = "&"# Affecte une valeur à 'my_rectangle_1.print_symbol'
print(my_rectangle_1)# Affiche à l'écran
print("--")# Affiche à l'écran

my_rectangle_2 = Rectangle(2, 1)# Affecte une valeur à 'my_rectangle_2'
print(my_rectangle_2)# Affiche à l'écran
print("--")# Affiche à l'écran
Rectangle.print_symbol = "C"# Affecte une valeur à 'Rectangle.print_symbol'
print(my_rectangle_2)# Affiche à l'écran
print("--")# Affiche à l'écran

my_rectangle_3 = Rectangle(7, 3)# Affecte une valeur à 'my_rectangle_3'
print(my_rectangle_3)# Affiche à l'écran

print("--")# Affiche à l'écran

my_rectangle_3.print_symbol = ["C", "is", "fun!"]# Affecte une valeur à 'my_rectangle_3.print_symbol'
print(my_rectangle_3)# Affiche à l'écran

print("--")# Affiche à l'écran
