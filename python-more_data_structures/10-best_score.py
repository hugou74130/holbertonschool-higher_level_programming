#!/usr/bin/python3

# Retourne la clé correspondant au meilleur score dans un dictionnaire
def best_score(a_dictionary):  # Définit la fonction 'best_score'
    """Retourne la clé ayant la plus grande valeur dans `a_dictionary`.

    Args:
        a_dictionary (dict): mapping nom->score.

    Returns:
        clé associée au score maximal, ou None si le dictionnaire est vide.
    """
    if not a_dictionary:  # Si le dictionnaire est vide
        return None  # Retourne None

    # Utilise `max` avec key=a_dictionary.get pour retourner la clé maximale
    return max(a_dictionary, key=a_dictionary.get)  # Retourne la clé du meilleur score
