#!/usr/bin/python3
import random# Importe le module 'random'

# Génère un nombre aléatoire entre -10000 et 10000 (inclus)
number = random.randint(-10000, 10000)# Affecte une valeur à 'number'

# Calcule la dernière digit du nombre en utilisant le modulo
last_digit = abs(number) % 10# Affecte une valeur à 'last_digit'

# Si le nombre est négatif, change la signe de la dernière digit pour qu'il soit négatif aussi
if number < 0:# Condition si
    last_digit = -last_digit    # Affecte une valeur à 'last_digit'

# Imprime la dernière digit du nombre avec un message et conditionnellement si elle est supérieure à 5, égale à 0 ou inférieure à 6 et différent de 0
print(f"Last digit of {number} is {last_digit}", end=" ")# Affiche à l'écran
if last_digit > 5:# Condition si
    print("and is greater than 5")    # Affiche à l'écran
elif last_digit == 0:# Sinon si
    print("and is 0")    # Affiche à l'écran
else:# Sinon
    print("and is less than 6 and not 0")    # Affiche à l'écran
