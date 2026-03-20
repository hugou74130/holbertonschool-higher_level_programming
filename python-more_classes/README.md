# Python - More Classes and Objects

Approfondissement de la POO Python : méthodes spéciales, attributs de classe, méthodes statiques et de classe.

## Utilisation

```bash
python3 <N>-main.py
```

## Tâches

Les tâches construisent progressivement une classe `Rectangle` :

| Fichier | Ajout par rapport au précédent |
| ------- | ------------------------------ |
| `0-rectangle.py` | Classe `Rectangle` vide |
| `1-rectangle.py` | Attributs `width` et `height` avec propriétés et validation |
| `2-rectangle.py` | Méthodes `area()` et `perimeter()` (retourne 0 si dimension nulle) |
| `3-rectangle.py` | Méthode `__str__` : affichage avec `#` |
| `4-rectangle.py` | Méthode `__repr__` : représentation officielle pour `eval()` |
| `5-rectangle.py` | Méthode `__del__` : message à la destruction de l'objet |
| `6-rectangle.py` | Attribut de classe `number_of_instances` : compteur d'instances actives |
| `7-rectangle.py` | Attribut de classe `print_symbol` : symbole d'affichage configurable |
| `8-rectangle.py` | Méthode statique `bigger_or_equal(rect_1, rect_2)` : compare deux rectangles |
| `9-rectangle.py` | Méthode de classe `square(cls, size)` : fabrique un rectangle carré |

## Concepts clés

- **Méthodes spéciales (dunder)** : `__str__`, `__repr__`, `__del__`
- **Attributs de classe** vs attributs d'instance
- **Méthode statique** `@staticmethod` — pas d'accès à `self` ni `cls`
- **Méthode de classe** `@classmethod` — reçoit `cls`, utilisée comme factory
- Comptage d'instances avec un attribut de classe partagé
- Symbole d'affichage configurable (instance ou classe)
- `eval(repr(obj))` — reconstruction d'un objet depuis sa représentation
