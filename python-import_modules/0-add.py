#!/usr/bin/python3

# Script d'exemple qui importe la fonction `add` depuis `add_0` et l'utilise
if __name__ == "__main__":  # Condition si exécuté en script
    from add_0 import add  # Importe la fonction 'add' depuis le module 'add_0'

    a = 1  # Premier nombre
    b = 2  # Second nombre

    # Affiche le résultat de l'addition
    print("{} + {} = {}".format(a, b, add(a, b)))  # Affiche à l'écran
