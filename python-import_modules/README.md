# Python - Import & Modules

Organisation du code Python en modules réutilisables et traitement des arguments en ligne de commande.

## Utilisation

```bash
python3 <fichier>.py [arguments...]
```

## Tâches

| Fichier | Description |
| ------- | ----------- |
| `0-add.py` | Importe `add` depuis `add_0.py` et affiche le résultat de `1 + 2 = 3` |
| `1-calculation.py` | Importe les 4 opérations de `calculator_1.py` et affiche leurs résultats |
| `2-args.py` | Affiche le nombre et la liste des arguments `argv` passés au script |
| `3-infinite_add.py` | Additionne tous les arguments entiers passés en ligne de commande |
| `5-variable_load.py` | Importe et affiche la variable `a` définie dans `variable_load_5.py` |

**Modules utilitaires :**

| Fichier | Rôle |
| ------- | ---- |
| `add_0.py` | Expose une fonction `add(a, b)` |
| `calculator_1.py` | Expose les fonctions `add`, `sub`, `mul`, `div` |
| `variable_load_5.py` | Expose la variable `a = 98` |

## Concepts clés

- `import module` et `from module import fonction`
- Garde `if __name__ == "__main__"` — empêche l'exécution lors de l'import
- `sys.argv` — liste des arguments passés en ligne de commande (`argv[0]` = nom du script)
- `len(sys.argv)` — nombre d'arguments
- Pluralisation dynamique dans les messages (`argument` vs `arguments`)
