#!/usr/bin/python3
"""Module pour écrire un fichier texte (UTF-8)."""  # Spécifie le but du module


def write_file(filename="", text=""):  # Définit la fonction avec deux paramètres : nom du fichier et texte à écrire
    """Écrit une chaîne de caractères dans un fichier texte (UTF-8).

    Args:
        filename (str): Nom du fichier.
        text (str): Texte à écrire.

    Returns:
        int: Nombre de caractères écrits.
    """
    with open(filename, "w", encoding="utf-8") as file:  # Ouvre le fichier en mode écriture (écrase le contenu existant), encodage UTF-8
        num = file.write(text)  # Écrit le texte dans le fichier et retourne le nombre de caractères écrits
    return num  # Retourne le nombre de caractères écrits dans le fichier
