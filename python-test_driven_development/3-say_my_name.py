#!/usr/bin/python3
"""Module définissant une fonction d'affichage de nom."""


def say_my_name(first_name, last_name=""):  # Définit la fonction 'say_my_name'
    """Affiche 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): prénom.
        last_name (str): nom (défaut : chaîne vide).

    Raises:
        TypeError: si `first_name` ou `last_name` n'est pas une chaîne.
    """
    # Validation des types pour respecter le contrat de la fonction
    if not isinstance(first_name, str):  # Condition si
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):  # Condition si
        raise TypeError("last_name must be a string")

    # Affiche le nom formaté
    print(f"My name is {first_name} {last_name}")  # Affiche à l'écran
