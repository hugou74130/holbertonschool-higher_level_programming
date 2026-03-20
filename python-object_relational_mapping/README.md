# Python - Object Relational Mapping

## Description

This project explores the use of **ORM (Object Relational Mapping)** in Python, bridging the gap between Python objects and a MySQL database. It is split into two parts:

1. **MySQLdb** – Using raw SQL queries with the `MySQLdb` module to interact with a MySQL database.
2. **SQLAlchemy** – Using the SQLAlchemy ORM to interact with the database through Python objects, without writing raw SQL.

---

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to `SELECT`, `INSERT`, `UPDATE`, and `DELETE` rows in a MySQL table
- What ORM means and why it is useful
- How to map a Python class to a MySQL table using SQLAlchemy
- How to avoid SQL injection vulnerabilities

---

## Requirements

- Python 3.8+
- MySQL 8.0+
- `MySQLdb` module (`mysqlclient`)
- `SQLAlchemy` 1.4+

### Installation

```bash
# Install MySQLdb
pip install mysqlclient

# Install SQLAlchemy
pip install SQLAlchemy
```

---

## Files

### Part 1 – Raw SQL with MySQLdb

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all states from the database, ordered by `id` |
| `1-filter_states.py` | Lists all states with a name starting with `N` |
| `2-my_filter_states.py` | Displays states matching a given name (user input) |
| `3-my_safe_filter_states.py` | Same as above but safe from SQL injection |
| `4-cities_by_state.py` | Lists all cities with their associated state names |
| `5-filter_cities.py` | Lists all cities of a given state (SQL injection safe) |

### Part 2 – ORM with SQLAlchemy

| File | Description |
|------|-------------|
| `model_state.py` | Defines the `State` class mapped to the `states` table |
| `model_city.py` | Defines the `City` class mapped to the `cities` table |
| `7-model_state_fetch_all.py` | Lists all `State` objects from the database |
| `8-model_state_fetch_first.py` | Prints the first `State` object |
| `9-model_state_filter_a.py` | Lists all states containing the letter `a` |
| `10-model_state_my_get.py` | Prints the id of a state matching a given name |
| `11-model_state_insert.py` | Adds a new `State` object to the database |
| `12-model_state_update_id_2.py` | Updates the name of the state with `id = 2` |
| `13-model_state_delete_a.py` | Deletes all states containing the letter `a` |
| `14-model_city_fetch_by_state.py` | Lists all `City` objects grouped by state |

---

## Usage

All scripts take the following arguments:

```bash
./script.py <mysql_username> <mysql_password> <database_name> [optional_arg]
```

### Examples

```bash
# List all states
./0-select_states.py root root hbtn_0e_0_usa

# List cities by state
./4-cities_by_state.py root root hbtn_0e_4_usa

# Filter cities of a specific state (SQL injection safe)
./5-filter_cities.py root root hbtn_0e_4_usa Texas

# Fetch all states with SQLAlchemy
./7-model_state_fetch_all.py root root hbtn_0e_6_usa

# Get state by name
./10-model_state_my_get.py root root hbtn_0e_6_usa California
```

---

## Models

### State (`model_state.py`)
```python
class State(Base):
    __tablename__ = 'states'
    id   = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
```

### City (`model_city.py`)
```python
class City(Base):
    __tablename__ = 'cities'
    id       = Column(Integer, primary_key=True, autoincrement=True)
    name     = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
```

---

## Author

**hugou74130** – [Holberton School](https://www.holbertonschool.com)