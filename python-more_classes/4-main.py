#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle# Affecte une valeur à 'Rectangle'

my_rectangle = Rectangle(2, 4)# Affecte une valeur à 'my_rectangle'
print(str(my_rectangle))# Affiche à l'écran
print("--")# Affiche à l'écran
print(my_rectangle)# Affiche à l'écran
print("--")# Affiche à l'écran
print(repr(my_rectangle))# Affiche à l'écran
print("--")# Affiche à l'écran
print(hex(id(my_rectangle)))# Affiche à l'écran
print("--")# Affiche à l'écran

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))# Affecte une valeur à 'new_rectangle'
print(str(new_rectangle))# Affiche à l'écran
print("--")# Affiche à l'écran
print(new_rectangle)# Affiche à l'écran
print("--")# Affiche à l'écran
print(repr(new_rectangle))# Affiche à l'écran
print("--")# Affiche à l'écran
print(hex(id(new_rectangle)))# Affiche à l'écran
print("--")# Affiche à l'écran

print(new_rectangle is my_rectangle)# Affiche à l'écran
print(type(new_rectangle) is type(my_rectangle))# Affiche à l'écran
