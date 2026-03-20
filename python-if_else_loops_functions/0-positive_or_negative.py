#!/usr/bin/python3

import random# Importe le module 'random'

# Génère un nombre aléatoire entre -10 et 10 (inclus)
number = random.randint(-10, 10)# Affecte une valeur à 'number'

# Vérifie si le nombre est positif, nul ou négatif et imprime le résultat
if number > 0:# Condition si
    print(f"{number} is positive")    # Affiche à l'écran
elif number == 0:# Sinon si
    print(f"{number} is zero")    # Affiche à l'écran
else:# Sinon
    print(f"{number} is negative")    # Affiche à l'écran
