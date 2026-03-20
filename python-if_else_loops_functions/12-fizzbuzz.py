#!/usr/bin/python3

# Définit une fonction qui affiche les nombres de 1 à 100,
# remplaçant les multiples de 3 par "Fizz",
# les multiples de 5 par "Buzz" et
# les multiples de both par "FizzBuzz"
def fizzbuzz():# Définit la fonction 'fizzbuzz'
    for i in range(1, 101):    # Boucle pour
        if i % 3 == 0 and i % 5 == 0:        # Condition si
            print("FizzBuzz", end=" ")            # Affiche à l'écran
        elif i % 3 == 0:        # Sinon si
            print("Fizz", end=" ")            # Affiche à l'écran
        elif i % 5 == 0:        # Sinon si
            print("Buzz", end=" ")            # Affiche à l'écran
        else:        # Sinon
            print(i, end=" ")            # Affiche à l'écran
