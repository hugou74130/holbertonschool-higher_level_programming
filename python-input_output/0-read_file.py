#!/usr/bin/python3
"""Module pour lire le contenu d'un fichier."""


def read_file(filename=""):# définit readfile avec comme paramettre filename
    """Lit et affiche le contenu d'un fichier."""
    with open(filename, "r", encoding="utf-8") as file: #ouvre le fichier en mode lecture avec l'encoding utf-8 
        print(file.read(), end="")# affiche le contenu du fichier
