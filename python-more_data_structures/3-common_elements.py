#!/usr/bin/python3

# Retourne l'intersection entre deux ensembles
def common_elements(set_1, set_2):  # Définit la fonction 'common_elements'
    """Retourne les éléments communs à `set_1` et `set_2`.

    Args:
        set_1 (set): premier ensemble.
        set_2 (set): second ensemble.

    Returns:
        set: nouvel ensemble contenant les éléments présents dans les deux sets.
    """
    # Utilise la méthode d'ensemble `intersection` pour obtenir la partie commune
    return set_1.intersection(set_2)  # Retourne le résultat
