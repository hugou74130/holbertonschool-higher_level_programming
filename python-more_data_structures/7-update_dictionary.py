#!/usr/bin/python3

# Met à jour (ou ajoute) la clé d'un dictionnaire avec une nouvelle valeur
def update_dictionary(a_dictionary, key, value):  # Définit la fonction 'update_dictionary'
    """Insère ou met à jour `key` dans `a_dictionary` avec `value` et retourne le dictionnaire.

    Args:
        a_dictionary (dict): dictionnaire cible.
        key: clé à insérer/mettre à jour.
        value: valeur à associer à la clé.

    Returns:
        dict: le dictionnaire mis à jour.
    """
    a_dictionary[key] = value  # Affecte une valeur à 'a_dictionary[key]'
    return a_dictionary  # Retourne le dictionnaire mis à jour
