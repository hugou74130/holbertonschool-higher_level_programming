#!/usr/bin/python3
"""Module pour indenter du texte.

La fonction `text_indentation` imprime le texte fourni en insérant
deux sauts de ligne après chaque point ('.'), point d'interrogation
('?') ou deux-points (':'). Les espaces en début de ligne sont
ignorés pour l'affichage propre.
"""


def text_indentation(text):  # Définit la fonction 'text_indentation'
    """Imprime `text` en ajoutant deux sauts de ligne après '.','?' et ':'.

    Args:
        text (str): la chaîne à afficher.

    Raises:
        TypeError: si `text` n'est pas une chaîne de caractères.
    """
    # Vérification du type d'entrée
    if not isinstance(text, str):  # Condition si
        raise TypeError("text must be a string")

    i = 0  # Indice de parcours dans la chaîne
    while i < len(text):  # Boucle principale jusqu'à la fin du texte
        # Ignorer les espaces en début de ligne (trim à gauche)
        while i < len(text) and text[i] == ' ':  # Boucle tant que
            i += 1  # Ignore les espaces

        # Imprime les caractères jusqu'à rencontrer une ponctuation cible
        while i < len(text):  # Boucle tant que
            print(text[i], end="")  # Affiche le caractère courant
            if text[i] in '.?:':  # Si caractère de ponctuation
                # Ajoute deux retours à la ligne (séparation de paragraphe)
                print("\n\n", end="")
                i += 1  # Passe au caractère suivant après la ponctuation
                break  # Recommence le cycle en ignorant les espaces initiaux
            i += 1  # Passe au caractère suivant
