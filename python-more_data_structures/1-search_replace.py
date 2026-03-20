#!/usr/bin/python3

# Remplace toutes les occurrences d'une valeur par une autre dans une liste
def search_replace(my_list, search, replace):  # Définit la fonction 'search_replace'
    """Retourne une nouvelle liste où chaque occurrence de `search` est remplacée par `replace`.

    Args:
        my_list (list): liste d'éléments.
        search: valeur à rechercher.
        replace: valeur de remplacement.

    Returns:
        list: nouvelle liste avec remplacements effectués.
    """
    # Compréhension de liste : maintient les éléments inchangés sauf lorsqu'ils sont égaux à `search`
    my_new_list = [replace if x == search else x for x in my_list]
    return my_new_list  # Retourne la nouvelle liste


# Exemple d'utilisation (externe) :
my_list = [1, 2, 3, 4, 5]  # Affecte une valeur à 'my_list'
