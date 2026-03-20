#!/usr/bin/python3

# Définit une fonction qui convertit un caractère en majuscule si possible
def uppercase(c):# Définit la fonction 'uppercase'
    # Vérifie si le code ASCII du caractère est entre 97 et 122 (inclus)
    if ord(c) >= 97 and ord(c) <= 122:    # Condition si
        return chr(ord(c) - 32)        # Retourne le résultat
    else:    # Sinon
        return c        # Retourne le résultat

# Exemple d'utilisation de la fonction
print(uppercase('a'))  # Devrait imprimer 'A'# Affiche à l'écran
print(uppercase('A'))  # Devrait imprimer 'A'# Affiche à l'écran
