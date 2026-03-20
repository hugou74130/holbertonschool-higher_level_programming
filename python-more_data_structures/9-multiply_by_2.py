#!/usr/bin/python3

# Retourne un nouveau dictionnaire où chaque valeur est multipliée par 2
def multiply_by_2(a_dictionary):  # Définit la fonction 'multiply_by_2'
    """Multiplie par 2 chaque valeur du dictionnaire et retourne un nouveau dictionnaire.

    Args:
        a_dictionary (dict): dictionnaire initial.

    Returns:
        dict: nouveau dictionnaire avec valeurs doublées.
    """
    # Utilise une compréhension dict pour créer un nouveau dictionnaire sans modifier l'original
    return {key: value * 2 for key, value in a_dictionary.items()}  # Retourne le résultat
