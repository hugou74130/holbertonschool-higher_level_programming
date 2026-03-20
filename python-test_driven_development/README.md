# Python - Test-Driven Development

Développement piloté par les tests (TDD) en Python : écriture de docstrings, tests doctest et tests unitaires avec `unittest`.

## Utilisation

```bash
# Lancer un fichier de test doctest
python3 -m doctest tests/<N>-<nom>.txt -v

# Lancer les tests unitaires
python3 -m unittest tests/6-max_integer_test.py
```

## Fichiers sources

| Fichier | Fonction | Description |
| ------- | -------- | ----------- |
| `0-add_integer.py` | `add_integer(a, b=98)` | Addition d'entiers avec conversion float→int et validation des types |
| `2-matrix_divided.py` | `matrix_divided(matrix, div)` | Divise tous les éléments d'une matrice par `div`, arrondi à 2 décimales |
| `3-say_my_name.py` | `say_my_name(first_name, last_name="")` | Affiche `My name is <first> <last>` avec validation des types |
| `4-print_square.py` | `print_square(size)` | Affiche un carré de `#` de taille `size` |
| `5-text_indentation.py` | `text_indentation(text)` | Ajoute 2 sauts de ligne après chaque `.`, `?` ou `:` |

## Fichiers de tests

| Fichier | Type | Ce qui est testé |
| ------- | ---- | ---------------- |
| `tests/0-add_integer.txt` | doctest | Cas normaux, floats, types invalides, valeurs extrêmes |
| `tests/2-matrix_divided.txt` | doctest | Matrices valides, division par zéro, types invalides, lignes inégales |
| `tests/3-say_my_name.txt` | doctest | Noms valides, types invalides, chaîne vide |
| `tests/4-print_square.txt` | doctest | Taille valide, zéro, types invalides, valeur négative |
| `tests/5-text_indentation.txt` | doctest | Ponctuation, espaces, chaîne vide |
| `tests/6-max_integer_test.py` | unittest | Tests de `max_integer()` : liste normale, un seul élément, liste vide, négatifs |

## Méthodologie TDD

1. Écrire les tests **avant** le code (fichiers `.txt` ou `.py` de test)
2. Vérifier que les tests échouent
3. Implémenter la fonction minimale pour les faire passer
4. Documenter chaque cas dans la docstring avec des exemples `doctest`

## Concepts clés

- **Docstrings** et exemples intégrés avec `>>>`
- **`doctest`** — module qui exécute les exemples dans les docstrings
- **`unittest`** — framework de tests unitaires (`TestCase`, `assertEqual`, `assertRaises`)
- Cas limites : types incorrects, valeurs nulles ou négatives, structures vides
