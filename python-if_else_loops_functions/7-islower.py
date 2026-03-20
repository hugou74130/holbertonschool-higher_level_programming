#!/usr/bin/python3

# Définit une fonction qui vérifie si un caractère est en minuscules
def islower(c):# Définit la fonction 'islower'
    # Vérifie si le code ASCII du caractère est entre 97 et 122 (inclus)
    return ord(c) >= 97 and ord(c) <= 122    # Retourne le résultat

# Exemple d'utilisation de la fonction
print(islower('a'))  # Devrait imprimer True# Affiche à l'écran
print(islower('A'))  # Devrait imprimer False# Affiche à l'écran
