#!/usr/bin/python3

# Déclare une longue chaîne `str` (utilise une continuation de ligne)
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"  # Affecte une valeur à 'str'

# Concatène des sous-parties de la chaîne via slicing pour former une nouvelle chaîne
str = str[39:67] + str[107:112] + str[0:6]  # Affecte une valeur à 'str'

# Affiche la chaîne résultante
print(str)  # Affiche à l'écran
