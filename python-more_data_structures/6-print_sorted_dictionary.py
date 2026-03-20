#!/usr/bin/python3

# Imprime un dictionnaire trié par clés
def print_sorted_dictionary(a_dictionary):  # Définit la fonction 'print_sorted_dictionary'
    """Imprime chaque paire clé: valeur du dictionnaire triée par clé.

    Args:
        a_dictionary (dict): le dictionnaire à afficher.
    """
    # Trie les clés et parcourt l'ordre trié pour affichage stable
    sorted_keys = sorted(a_dictionary.keys())  # Affecte une valeur à 'sorted_keys'

    for key in sorted_keys:  # Boucle pour chaque clé triée
        print("{}: {}".format(key, a_dictionary[key]))  # Affiche la paire
