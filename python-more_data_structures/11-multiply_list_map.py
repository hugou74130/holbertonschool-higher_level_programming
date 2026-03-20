#!/usr/bin/python3

# Multiplie chaque élément d'une liste par un nombre en utilisant map
def multiply_list_map(my_list=[], number=0):  # Définit la fonction 'multiply_list_map'
    """Retourne une nouvelle liste où chaque élément de `my_list` est multiplié par `number`.

    Args:
        my_list (list): liste d'entiers.
        number (int): multiplicateur.

    Returns:
        list: nouvelle liste des produits.
    """
    # Utilise map + lambda pour conserver une approche fonctionnelle
    return list(map(lambda x: x * number, my_list))  # Retourne le résultat
