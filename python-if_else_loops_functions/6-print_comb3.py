#!/usr/bin/python3

# Boucle à travers les nombres de 0 à 999 en trois chiffres
for i in range(1000):# Boucle pour
    # Convertit le nombre en chaîne de caractères et ajoute des zéros devant si nécessaire
    if i < 10:    # Condition si
        print("00", end="")        # Affiche à l'écran
    elif i < 100:    # Sinon si
        print("0", end="")        # Affiche à l'écran
    print(i, end=" ")    # Affiche à l'écran
