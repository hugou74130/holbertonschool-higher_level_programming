#!/usr/bin/python3
"""Module fournissant une fonction pour imprimer un carré avec '#'."""


def print_square(size):  # Définit la fonction 'print_square'
    """Imprime un carré composé du caractère '#' de côté `size`.

    Args:
        size (int): taille du côté du carré.

    Raises:
        TypeError: si `size` n'est pas un entier.
        ValueError: si `size` est négatif.
    """
    # Vérifie que la taille est bien un entier
    if not isinstance(size, int):  # Condition si
        # Le code original lève TypeError même pour certains floats ; on ne change pas la logique
        if isinstance(size, float) and size < 0:  # Condition si
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    # Vérifie que la taille n'est pas négative
    if size < 0:  # Condition si
        raise ValueError("size must be >= 0")

    # Imprime `size` lignes contenant `size` fois le caractère '#'
    for _ in range(size):  # Boucle pour
        print('#' * size)  # Affiche à l'écran
