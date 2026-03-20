# Python - Input/Output

Opérations de lecture/écriture de fichiers et sérialisation JSON en Python.

## Utilisation

```bash
python3 <N>-main.py
# ou pour 7-add_item.py (utilitaire CLI)
python3 7-add_item.py <arg1> <arg2> ...
```

## Tâches

| Fichier | Fonction/Classe | Description |
| ------- | --------------- | ----------- |
| `0-read_file.py` | `read_file(filename)` | Lit et affiche le contenu d'un fichier texte (UTF-8) |
| `1-write_file.py` | `write_file(filename, text)` | Écrit une chaîne dans un fichier, retourne le nombre de caractères écrits |
| `2-append_write.py` | `append_write(filename, text)` | Ajoute une chaîne à la fin d'un fichier, retourne le nombre de caractères ajoutés |
| `3-to_json_string.py` | `to_json_string(my_obj)` | Retourne la représentation JSON (chaîne) d'un objet |
| `4-from_json_string.py` | `from_json_string(my_str)` | Retourne l'objet Python correspondant à une chaîne JSON |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)` | Sauvegarde un objet dans un fichier JSON |
| `6-load_from_json_file.py` | `load_from_json_file(filename)` | Charge et retourne un objet Python depuis un fichier JSON |
| `7-add_item.py` | — | Script CLI : charge `add_item.json`, ajoute les arguments `argv`, sauvegarde |
| `8-class_to_json.py` | `class_to_json(an_object)` | Retourne le dictionnaire des attributs sérialisables d'une instance |
| `9-student.py` | `Student` | Classe avec `to_json()` retournant tous les attributs |
| `10-student.py` | `Student` | Idem avec `to_json(attrs)` filtrant par liste d'attributs |
| `11-student.py` | `Student` | Ajout de `reload_from_json(json)` pour désérialiser un dictionnaire |
| `12-pascal_triangle.py` | `pascal_triangle(n)` | Retourne le triangle de Pascal jusqu'à la ligne `n` |

## Concepts clés

- **Gestionnaire de contexte** `with open(...) as f` — fermeture automatique du fichier
- Modes d'ouverture : `"r"` (lecture), `"w"` (écriture/écrase), `"a"` (ajout)
- Encodage `encoding="utf-8"`
- **Module `json`** : `json.dumps()`, `json.loads()`, `json.dump()`, `json.load()`
- Sérialisation de classe : `__dict__` pour obtenir les attributs d'une instance
- Argument `sys.argv` pour les scripts CLI
- Algorithme : triangle de Pascal avec listes imbriquées
