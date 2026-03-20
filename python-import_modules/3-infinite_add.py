#!/usr/bin/python3

# Script qui additionne des nombres fournis en arguments du script
from sys import argv  # Importe depuis le module 'sys'

if __name__ == "__main__":  # Condition si exécuté en tant que script
    total = 0  # Initialise le total

    # Parcourt les arguments fournis (excluant le nom du script)
    for i in range(1, len(argv)):
        # Convertit chaque argument en entier et l'ajoute au total
        total += int(argv[i])

# Affiche la somme calculée
print(total)  # Affiche à l'écran
