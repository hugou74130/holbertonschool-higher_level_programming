# Python - Inheritance

Héritage en Python : hiérarchies de classes, vérification de types et classes de base abstraites.

## Utilisation

```bash
python3 <N>-main.py

# Exécuter les tests doctest
python3 -m doctest tests/<N>-<nom>.txt -v
```

## Tâches

| Fichier | Contenu |
| ------- | ------- |
| `0-lookup.py` | Fonction `lookup(obj)` : retourne la liste des attributs et méthodes d'un objet |
| `1-my_list.py` | Classe `MyList(list)` avec méthode `print_sorted()` qui affiche la liste triée |
| `2-is_same_class.py` | Fonction `is_same_class(obj, a_class)` : `True` uniquement si `obj` est exactement une instance de `a_class` |
| `3-is_kind_of_class.py` | Fonction `is_kind_of_class(obj, a_class)` : `True` si instance directe ou sous-classe |
| `4-inherits_from.py` | Fonction `inherits_from(obj, a_class)` : `True` si sous-classe **stricte** (pas la classe elle-même) |
| `5-base_geometry.py` | Classe `BaseGeometry` vide |
| `6-base_geometry.py` | `BaseGeometry` avec méthode `area()` levant `Exception("area() is not implemented")` |
| `7-base_geometry.py` | Ajout de `integer_validator(name, value)` : valide qu'une valeur est un entier positif |
| `8-rectangle.py` | Classe `Rectangle(BaseGeometry)` avec validation `width` et `height` via `integer_validator` |
| `9-rectangle.py` | `Rectangle` avec `__str__` : `[Rectangle] width/height` |
| `10-square.py` | Classe `Square(Rectangle)` avec validation `size` |
| `11-square.py` | `Square` avec `__str__` : `[Square] size/size` |

## Tests doctest

```bash
python3 -m doctest tests/1-my_list.txt -v
python3 -m doctest tests/7-base_geometry.txt -v
```

## Hiérarchie des classes

```text
object
  └── BaseGeometry
        └── Rectangle
              └── Square
```

## Concepts clés

- `class Enfant(Parent)` — syntaxe d'héritage
- `isinstance(obj, classe)` — vérifie instance (inclut sous-classes)
- `issubclass(sous_classe, classe)` — vérifie la relation d'héritage
- `type(obj) is classe` — vérifie le type exact (sans héritage)
- `super()` — appel du constructeur ou d'une méthode parent
- Méthode abstraite simulée : `raise Exception("not implemented")`
- Tests doctest dans `tests/`
