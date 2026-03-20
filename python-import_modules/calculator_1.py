#!/usr/bin/python3

# Module fournissant des opérations arithmétiques de base

def add(a, b):  # Définit la fonction 'add'
    """Retourne la somme de `a` et `b`.

    Args:
        a: premier opérande (nombre).
        b: second opérande (nombre).

    Returns:
        La somme `a + b`.
    """
    return (a + b)  # Retourne le résultat


def sub(a, b):  # Définit la fonction 'sub'
    """Retourne la différence `a - b`.

    Args:
        a: premier opérande (nombre).
        b: second opérande (nombre).

    Returns:
        La différence `a - b`.
    """
    return (a - b)  # Retourne le résultat


def mul(a, b):  # Définit la fonction 'mul'
    """Retourne le produit `a * b`.

    Args:
        a: premier opérande (nombre).
        b: second opérande (nombre).

    Returns:
        Le produit `a * b`.
    """
    return (a * b)  # Retourne le résultat


def div(a, b):  # Définit la fonction 'div'
    """Effectue la division `a / b` et retourne un entier (int).

    Note: le résultat est converti en `int` dans cette implémentation.

    Args:
        a: dividende (nombre).
        b: diviseur (nombre).

    Returns:
        Le quotient converti en entier (`int(a / b)`).
    """
    return int(a / b)  # Retourne le résultat (conversion en int)
