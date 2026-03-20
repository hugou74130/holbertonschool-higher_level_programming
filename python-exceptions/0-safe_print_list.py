#!/usr/bin/python3

# Imprime jusqu'à `x` éléments de la liste en gérant les IndexError
def safe_print_list(my_list=[], x=0):  # Définit la fonction 'safe_print_list'
    """Imprime `x` éléments de `my_list` et retourne le nombre d'éléments imprimés.

    Si `x` est supérieur à la longueur de la liste, la fonction s'arrête proprement.
    """
    count = 0  # Compteur d'éléments imprimés
    for i in range(x):  # Parcourt les indices demandés
        try:  # Essaye d'accéder à l'élément
            print(my_list[i], end='')  # Imprime l'élément sans saut de ligne
            count += 1  # Incrémente le compteur
        except IndexError:  # Si l'index n'existe pas, on arrête la boucle
            break
    print()  # Ajoute un saut de ligne final
    return count  # Retourne le nombre d'éléments imprimés
