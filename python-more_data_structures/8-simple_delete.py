#!/usr/bin/python3

# Supprime une clé d'un dictionnaire si elle existe
def simple_delete(a_dictionary, key=""):  # Définit la fonction 'simple_delete'
    """Supprime `key` de `a_dictionary` si présente et retourne le dictionnaire.

    Args:
        a_dictionary (dict): le dictionnaire d'origine.
        key: clé à supprimer si elle existe.

    Returns:
        dict: le dictionnaire (modifié ou non).
    """
    if key in a_dictionary:  # Condition si la clé existe
        del a_dictionary[key]  # Supprime la paire clé:valeur
    return a_dictionary  # Retourne le dictionnaire
