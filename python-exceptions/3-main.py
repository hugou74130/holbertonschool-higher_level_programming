#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division# Affecte une valeur à 'safe_print_division'

a = 12# Affecte une valeur à 'a'
b = 2# Affecte une valeur à 'b'
result = safe_print_division(a, b)# Affecte une valeur à 'result'
print("{:d} / {:d} = {}".format(a, b, result))# Affiche à l'écran

a = 12# Affecte une valeur à 'a'
b = 0# Affecte une valeur à 'b'
result = safe_print_division(a, b)# Affecte une valeur à 'result'
print("{:d} / {:d} = {}".format(a, b, result))# Affiche à l'écran
