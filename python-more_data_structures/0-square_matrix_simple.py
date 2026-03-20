#!/usr/bin/python3

# Retourne une nouvelle matrice où chaque élément est le carré de l'original
def square_matrix_simple(matrix=[]):  # Définit la fonction 'square_matrix_simple'
    """Calcule le carré de chaque élément dans une matrice (liste de listes).

    Args:
        matrix (list of list): matrice d'entiers.

    Returns:
        list of list: nouvelle matrice contenant les carrés des éléments.
    """
    # Utilise une compréhension imbriquée pour conserver la structure ligne/colonne
    return [[num ** 2 for num in row] for row in matrix]  # Retourne le résultat
