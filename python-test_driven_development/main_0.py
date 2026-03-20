#!/usr/bin/python3

add_integer = __import__('0-add_integer').add_integer# Affecte une valeur à 'add_integer'

print(add_integer(1, 2))  # Expected: 3# Affiche à l'écran
print(add_integer(100, -2))  # Expected: 98# Affiche à l'écran
print(add_integer(2))  # Expected: 100# Affiche à l'écran
print(add_integer(100.3, -2))  # Expected: 98# Affiche à l'écran
try:# Bloc try
    print(add_integer(4, "School"))  # Should raise TypeError    # Affiche à l'écran
except Exception as e:# Capture l'exception
    print(e)  # Expected output: a must be an integer or b must be an integer    # Affiche à l'écran

try:# Bloc try
    print(add_integer(None))  # Should raise TypeError    # Affiche à l'écran
except Exception as e:# Capture l'exception
    print(e)  # Expected output: a must be an integer or b must be an integer    # Affiche à l'écran
