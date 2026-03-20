#!/usr/bin/python3

# Convertit un nombre romain en entier
def roman_to_int(roman_string):  # Définit la fonction 'roman_to_int'
    """Convertit une chaîne romaine valide en entier.

    Args:
        roman_string (str): chaîne représentant un nombre en chiffres romains.

    Returns:
        int: valeur entière correspondante, ou 0 si l'entrée n'est pas une chaîne.
    """
    # Vérifie le type d'entrée
    if not isinstance(roman_string, str) or roman_string is None:
        return 0  # Retourne 0 si l'entrée n'est pas une chaîne valide

    # Mapping des symboles romains vers leurs valeurs
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0  # Valeur accumulée
    i = 0  # Indice de parcours

    # Parcours de la chaîne en tenant compte des combinaisons soustractives (ex: IV = 4)
    while i < len(roman_string):
        # Si le symbole courant est inférieur au suivant, on soustrait
        if (i + 1 < len(roman_string) and
                roman_map[roman_string[i]] < roman_map[roman_string[i + 1]]):
            total += (roman_map[roman_string[i + 1]] - roman_map[roman_string[i]])
            i += 2  # Avance de 2 positions lorsque l'on traite une paire
        else:
            total += roman_map[roman_string[i]]
            i += 1
    return total  # Retourne la valeur entière calculée
