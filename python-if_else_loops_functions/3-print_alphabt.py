#!/usr/bin/python3

# Boucle à travers les codes ASCII pour les lettres minuscules de 'a' à 'z'
for i in range(97, 123):# Boucle pour
    # Vérifie si le code ASCII n'est pas celui de 'e' (101) ou de 'q' (113)
    if i != 101 and i != 113:    # Condition si
        # Convertit le code ASCII en caractère et l'imprime avec un espace final
        print("{}".format(chr(i)), end="")        # Affiche à l'écran
