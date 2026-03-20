#!/usr/bin/python3
"""Module fournissant une fonction d'addition d'entiers.

Ce module définit la fonction `add_integer` qui additionne deux
valeurs numériques après les convertir en entiers (via int()).
"""


def add_integer(a, b=98):  # Définit la fonction 'add_integer'
    """Additionne `a` et `b` puis retourne un entier.

    La fonction accepte des entiers et des floats (les floats sont
    convertis en `int` avant l'addition). Si un paramètre n'est pas
    numérique, une exception TypeError est levée.

    Args:
        a (int|float): premier opérande.
        b (int|float, optional): second opérande (par défaut 98).

    Returns:
        int: résultat de int(a) + int(b).
    """
    # Vérification du type : on accepte int ou float uniquement
    if not isinstance(a, (int, float)):  # Condition si
        raise TypeError("a must be an integer")  # On respecte l'API demandée
    if not isinstance(b, (int, float)):  # Condition si
        raise TypeError("b must be an integer")

    # Cas particuliers pour les floats non finis ou NaN : on les rejette explicitement
    if isinstance(a, float) and (a != a or a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    # Conversion en int suivie de l'addition — conforme au cahier des charges
    return int(a) + int(b)  # Retourne le résultat
