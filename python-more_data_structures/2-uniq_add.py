#!/usr/bin/python3

# Somme des éléments uniques d'une liste
def uniq_add(my_list=[]):  # Définit la fonction 'uniq_add'
    """Retourne la somme des éléments uniques dans `my_list`.

    Args:
        my_list (list): liste d'entiers.

    Returns:
        int: somme des valeurs uniques.
    """
    # Transformer en set supprime les doublons ; sum calcule la somme des éléments uniques
    return sum(set(my_list))  # Retourne le résultat
