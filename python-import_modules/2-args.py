#!/usr/bin/python3

# Script affichant les arguments passés au programme
from sys import argv  # Importe depuis le module 'sys'

if __name__ == "__main__":  # Condition si exécuté en tant que script
    nb_args = len(argv) - 1  # Calcule le nombre d'arguments (hors nom du script)

    # Affiche un message adapté selon le nombre d'arguments
    if nb_args == 0:
        print("0 arguments.")
    elif nb_args == 1:
        print("1 argument:")
    else:
        print(f"{nb_args} arguments:")

    # Énumère et affiche chaque argument avec son indice
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
