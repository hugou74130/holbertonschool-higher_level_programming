#!/usr/bin/python3

# Script d'exemple utilisant des fonctions arithmétiques importées depuis `calculator_1`
from calculator_1 import add, sub, mul, div  # Importe depuis le module 'calculator_1'

if __name__ == "__main__":  # Condition si exécuté en tant que script
    a = 10  # Premier opérande
    b = 5  # Second opérande

    # Affiche les résultats des opérations de base
    print("{} + {} = {}".format(a, b, add(a, b)))  # Somme
    print("{} - {} = {}".format(a, b, sub(a, b)))  # Différence
    print("{} * {} = {}".format(a, b, mul(a, b)))  # Produit
    print("{} / {} = {}".format(a, b, div(a, b)))  # Quotient
