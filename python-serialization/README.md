# Python - Serialization

Sérialisation de données en Python : JSON, Pickle, CSV et XML.

## Utilisation

```bash
python3 <fichier>.py
```

## Tâches

| Fichier | Description |
| ------- | ----------- |
| `task_00_basic_serialization.py` | Fonctions `serialize_and_save_to_file(data, filename)` et `load_and_deserialize(filename)` avec le module `json` |
| `task_01_pickle.py` | Classe `CustomObject` avec `serialize(filename)` et `deserialize(filename)` via le module `pickle` |
| `task_02_csv.py` | Fonction `convert_csv_to_json(csv_filename)` qui convertit un fichier CSV en JSON |
| `task_03_xml.py` | Fonctions `serialize_to_xml(dictionary, filename)` et `deserialize_from_xml(filename)` via `xml.etree.ElementTree` |

## Comparaison des formats

| Format | Module Python | Usage typique | Interopérabilité |
| ------ | ------------- | ------------- | ---------------- |
| JSON | `json` | APIs web, configs | Universel |
| Pickle | `pickle` | Objets Python complexes | Python uniquement |
| CSV | `csv` | Données tabulaires | Universel |
| XML | `xml.etree.ElementTree` | Configs, données structurées | Universel |

## Concepts clés

- **JSON** : `json.dumps()` / `json.loads()` pour chaînes, `json.dump()` / `json.load()` pour fichiers
- **Pickle** : `pickle.dumps()` / `pickle.loads()`, sérialise n'importe quel objet Python (y compris les instances de classe)
- **CSV** : `csv.DictReader` pour lire, `csv.DictWriter` pour écrire ; conversion vers JSON avec `json.dump()`
- **XML** : `ET.Element()`, `ET.SubElement()`, `ET.parse()` ; écriture avec `ET.indent()` et `ET.write()`
- Encodage UTF-8 dans les opérations de fichiers
