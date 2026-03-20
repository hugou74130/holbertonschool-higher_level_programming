#!/usr/bin/python3

# Différence symétrique entre deux ensembles
def only_diff_elements(set_1, set_2):  # Définit la fonction 'only_diff_elements'
    """Retourne les éléments présents dans l'un ou l'autre set mais pas dans les deux.

    Args:
        set_1 (set): premier ensemble.
        set_2 (set): second ensemble.

    Returns:
        set: différence symétrique des deux ensembles.
    """
    # L'opérateur ^ réalise la différence symétrique (éléments exclusifs à chaque set)
    return set_1 ^ set_2  # Retourne le résultat
