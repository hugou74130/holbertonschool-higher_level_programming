# SQL - More Queries

Approfondissement du SQL avec MySQL : gestion des utilisateurs, contraintes, jointures et sous-requêtes.

## Prérequis

- MySQL 8.0+
- Droits administrateur pour les tâches de gestion d'utilisateurs (0-2)

## Utilisation

```bash
# Exécuter un fichier sur une base de données
cat <fichier>.sql | mysql -uroot -p <nom_de_base>

# Pour les fichiers qui créent leur propre base (6-states, 7-cities...)
cat <fichier>.sql | mysql -uroot -p
```

Pour les tâches 10 à 16, importer d'abord la base TV shows fournie par Holberton :

```bash
cat hbtn_0d_tvshows.sql | mysql -uroot -p hbtn_0d_tvshows
```

## Tâches

| Fichier | Description |
| ------- | ----------- |
| `0-privileges.sql` | Affiche les droits de `user_0d_1` et `user_0d_2` (`SHOW GRANTS`) |
| `1-create_user.sql` | Crée `user_0d_1` avec tous les privilèges sur toutes les bases |
| `2-create_read_user.sql` | Crée la base `hbtn_0d_2` et `user_0d_2` avec droits `SELECT` uniquement |
| `3-force_name.sql` | Crée `force_name` avec colonne `name VARCHAR(256) NOT NULL` |
| `4-never_empty.sql` | Crée `id_not_null` avec `id INT DEFAULT 1` |
| `5-unique_id.sql` | Crée `unique_id` avec `id INT DEFAULT 1 UNIQUE` |
| `6-states.sql` | Crée la base `hbtn_0d_usa` et la table `states` (id AUTO_INCREMENT PRIMARY KEY) |
| `7-cities.sql` | Crée `cities` avec clé étrangère `state_id` vers `states(id)` |
| `8-cities_of_california_subquery.sql` | Liste les villes de Californie via sous-requête (sans JOIN) |
| `9-cities_by_state_join.sql` | Liste toutes les villes avec le nom de leur état via `INNER JOIN` |
| `10-genre_id_by_show.sql` | Affiche les `genre_id` des séries ayant au moins un genre (`INNER JOIN`) |
| `11-genre_id_all_shows.sql` | Affiche les `genre_id` de toutes les séries, `NULL` si aucun genre (`LEFT JOIN`) |
| `12-no_genre.sql` | Liste les séries sans genre (`LEFT JOIN` + `WHERE genre_id IS NULL`) |
| `13-count_shows_by_genre.sql` | Compte les séries par genre, trié par nombre décroissant |
| `14-my_genres.sql` | Liste les genres de la série `Dexter` (double `JOIN`) |
| `15-comedy_only.sql` | Liste toutes les séries du genre `Comedy` (double `JOIN`) |
| `16-shows_by_genre.sql` | Liste toutes les séries avec leurs genres, `NULL` si aucun (double `LEFT JOIN`) |

## Schéma de la base TV Shows

```text
tv_shows          tv_show_genres        genres
---------         --------------        ------
id (PK)  <------  tv_show_id (FK)       id (PK)
title            genre_id (FK)  ------> name
```

## Concepts clés

- **Gestion des utilisateurs** : `CREATE USER IF NOT EXISTS`, `GRANT`, `FLUSH PRIVILEGES`, `SHOW GRANTS`
- **Contraintes de table** : `NOT NULL`, `DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `AUTO_INCREMENT`, `FOREIGN KEY ... REFERENCES`
- **Jointures** :
  - `INNER JOIN` — uniquement les lignes avec correspondance dans les deux tables
  - `LEFT JOIN` — toutes les lignes de la table gauche, `NULL` si pas de correspondance à droite
- **Sous-requête** — requête imbriquée dans une clause `WHERE`
- **Agrégation** : `COUNT()`, `GROUP BY`, `ORDER BY`
