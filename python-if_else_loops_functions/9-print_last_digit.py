#!/usr/bin/python3

# Définit une fonction qui retourne et imprime la dernière digit d'un nombre
def print_last_digit(number):# Définit la fonction 'print_last_digit'
    last_digit = abs(number) % 10    # Affecte une valeur à 'last_digit'
    if number < 0:    # Condition si
        last_digit = -last_digit        # Affecte une valeur à 'last_digit'
    print(f"Last digit of {number} is {last_digit}", end=" ")    # Affiche à l'écran
    return last_digit    # Retourne le résultat

# Exemple d'utilisation de la fonction
print_last_digit(98)# Code
