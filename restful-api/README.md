# Python - RESTful API

Introduction aux APIs REST en Python : clients HTTP, serveur basique, Flask, authentification et documentation Swagger.

## Prérequis

```bash
pip install requests flask flask-httpauth flask-jwt-extended flasgger
```

## Tâches

| Fichier | Description | Port |
| ------- | ----------- | ---- |
| `task_02_requests.py` | Client HTTP avec `requests` : GET/POST sur une API externe (JSONPlaceholder) | — |
| `task_03_http_server.py` | Serveur HTTP basique avec `http.server` : routes `/`, `/data`, `/status`, `/info` | 8000 |
| `task_04_flask.py` | API Flask avec routes JSON : `GET /`, `/data`, `/status`, `/users/<username>`, `POST /add_user` | 5000 |
| `task_05_basic_security.py` | Sécurité Flask : HTTP Basic Auth (`flask-httpauth`) + JWT (`flask-jwt-extended`) | 5000 |
| `task_06_swagger_example.py` | Documentation OpenAPI/Swagger de l'API Flask avec `flasgger` | 5000 |

## Lancer les serveurs

```bash
# Serveur basique
python3 task_03_http_server.py

# API Flask
python3 task_04_flask.py

# API Flask avec auth
python3 task_05_basic_security.py

# API Flask avec Swagger (docs sur http://localhost:5000/apidocs)
python3 task_06_swagger_example.py
```

## Tester les endpoints

```bash
# GET simple
curl http://localhost:5000/status

# POST avec JSON
curl -X POST http://localhost:5000/add_user \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "name": "Alice", "age": 30}'

# Avec Basic Auth (task_05)
curl -u user1:password http://localhost:5000/basic-protected

# Avec JWT (task_05)
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "password"}'
```

## Concepts clés

- **Méthodes HTTP** : `GET`, `POST`, `PUT`, `DELETE`
- **Codes de statut** : `200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `409 Conflict`
- **Flask** : `@app.route()`, `request.get_json()`, `jsonify()`
- **Authentification** : HTTP Basic Auth, JWT (JSON Web Token)
- **OpenAPI/Swagger** : documentation auto-générée des endpoints
- **`requests`** : `requests.get()`, `requests.post()`, gestion des réponses JSON
