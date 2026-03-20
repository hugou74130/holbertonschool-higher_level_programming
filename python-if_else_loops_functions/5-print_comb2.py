#!/usr/bin/python3

# Boucle à travers les nombres de 0 à 99 en deux chiffres
for i in range(100):# Boucle pour
    # Convertit le nombre en chaîne de caractères et ajoute un zéro devant si nécessaire
    if i < 10:    # Condition si
        print("0", end="")        # Affiche à l'écran
    print(i, end=" ")    # Affiche à l'écran
