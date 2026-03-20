# SQL - Introduction

Découverte du langage SQL avec MySQL : création de bases de données, manipulation de données et requêtes de sélection.

## Prérequis

- MySQL 8.0+
- Accès à un serveur MySQL (local ou distant)

## Utilisation

Les fichiers `.sql` s'exécutent via le client MySQL :

```bash
# Exécuter un fichier sur une base de données existante
cat <fichier>.sql | mysql -uroot -p <nom_de_base>

# Pour les fichiers qui créent/suppriment une base (tâches 0-3)
cat <fichier>.sql | mysql -uroot -p
```

## Tâches

| Fichier | Description |
| ------- | ----------- |
| `0-list_databases.sql` | Affiche toutes les bases de données (`SHOW DATABASES`) |
| `1-create_database_if_missing.sql` | Crée `hbtn_0c_0` si elle n'existe pas (`CREATE DATABASE IF NOT EXISTS`) |
| `2-remove_database.sql` | Supprime `hbtn_0c_0` si elle existe (`DROP DATABASE IF EXISTS`) |
| `3-list_tables.sql` | Liste toutes les tables de la base courante (`SHOW TABLES`) |
| `4-first_table.sql` | Crée `first_table` avec les colonnes `id INT` et `name VARCHAR(256)` |
| `5-full_table.sql` | Affiche la structure complète de `first_table` (`SHOW CREATE TABLE`) |
| `6-list_values.sql` | Affiche toutes les lignes de `first_table` (`SELECT *`) |
| `7-insert_value.sql` | Insère la ligne `(89, 'Best School')` dans `first_table` |
| `8-count_89.sql` | Compte le nombre de lignes avec `id = 89` |
| `9-full_creation.sql` | Crée `second_table` et insère 4 enregistrements (id, name, score) |
| `10-top_score.sql` | Liste `score` et `name` de `second_table` triés par score décroissant |
| `11-best_score.sql` | Liste les enregistrements avec `score >= 10`, triés par score décroissant |
| `12-no_cheating.sql` | Met à jour le score de `Bob` à `10` (sans utiliser son `id`) |
| `13-change_class.sql` | Supprime les lignes avec `score <= 5` |
| `14-average.sql` | Calcule la moyenne des scores (`AVG`) |
| `15-groups.sql` | Liste les scores distincts avec leur nombre d'occurrences, triés par fréquence |
| `16-no_link.sql` | Liste `score` et `name` en excluant les lignes sans nom, triés par score |

## Concepts clés

- **DDL** (Data Definition Language) : `CREATE`, `DROP`, `SHOW`
- **DML** (Data Manipulation Language) : `INSERT`, `UPDATE`, `DELETE`
- **DQL** (Data Query Language) : `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`
- Fonctions d'agrégation : `COUNT`, `AVG`
- Contraintes : `IF NOT EXISTS`, `IF EXISTS`
