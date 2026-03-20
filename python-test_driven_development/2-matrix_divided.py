#!/usr/bin/python3
"""Module fournissant une fonction pour diviser tous les éléments d'une matrice."""


def matrix_divided(matrix, div):  # Définit la fonction 'matrix_divided'
    """Divise chaque élément d'une matrice par `div` et retourne une nouvelle matrice.

    Args:
        matrix (list of list): matrice (liste de listes) d'entiers ou floats.
        div (int|float): diviseur (non nul).

    Returns:
        list of list: nouvelle matrice avec chaque valeur arrondie à 2 décimales.

    Raises:
        TypeError: si la structure de la matrice est invalide ou si `div` n'est pas un nombre.
        ZeroDivisionError: si `div` vaut 0.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Vérifie que matrix est une liste non vide
    if not isinstance(matrix, list) or len(matrix) == 0:  # Condition si
        raise TypeError(error_msg)

    # Vérifie que chaque ligne est une liste non vide et contient uniquement des nombres
    for row in matrix:  # Boucle pour
        if not isinstance(row, list) or len(row) == 0:  # Condition si
            raise TypeError(error_msg)
        for elem in row:  # Boucle pour
            if not isinstance(elem, (int, float)):  # Condition si
                raise TypeError(error_msg)

    # Vérifie que toutes les lignes ont la même longueur
    row_size = len(matrix[0])  # Affecte une valeur à 'row_size'
    for row in matrix:  # Boucle pour
        if len(row) != row_size:  # Condition si
            raise TypeError("Each row of the matrix must have the same size")

    # Vérifie que div est bien un nombre (int ou float)
    if not isinstance(div, (int, float)):  # Condition si
        raise TypeError("div must be a number")

    # Empêche la division par zéro
    if div == 0:  # Condition si
        raise ZeroDivisionError("division by zero")

    # Effectue la division et arrondit chaque résultat à 2 décimales
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix  # Retourne le résultat
