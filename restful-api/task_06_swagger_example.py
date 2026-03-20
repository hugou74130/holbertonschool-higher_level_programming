#!/usr/bin/python3
"""
Petit exemple Flask + OpenAPI (Swagger) minimal — aucun module supplémentaire requis.

- Lance : python3 task_06_swagger_example.py
- Ouvre dans le navigateur : https://petstore.swagger.io/?url=http://localhost:5000/openapi.json
  (Swagger UI affichera automatiquement la documentation basée sur /openapi.json)
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
_items = [{"id": 1, "name": "apple"}]


@app.route("/items", methods=["GET"])
def get_items():
    """Retourne la liste des items"""
    return jsonify(_items)


@app.route("/items", methods=["POST"])
def create_item():
    """Crée un item simple à partir d'un JSON {"name": "..."}"""
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return jsonify({"error": "name required"}), 400
    item = {"id": len(_items) + 1, "name": name}
    _items.append(item)
    return jsonify(item), 201


@app.route("/openapi.json")
def openapi_spec():
    """Renvoie une spec OpenAPI minimale décrivant /items"""
    spec = {
        "openapi": "3.0.0",
        "info": {"title": "Simple API", "version": "1.0.0"},
        "paths": {
            "/items": {
                "get": {
                    "summary": "List items",
                    "responses": {
                        "200": {
                            "description": "A list of items",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "array", "items": {"type": "object"}}
                                }
                            },
                        }
                    },
                },
                "post": {
                    "summary": "Create an item",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {"name": {"type": "string"}},
                                    "required": ["name"],
                                }
                            }
                        },
                    },
                    "responses": {
                        "201": {"description": "Item created"},
                        "400": {"description": "Bad request"},
                    },
                },
            }
        },
    }
    return jsonify(spec)


@app.route('/docs')
def swagger_ui():
    """Serve a minimal Swagger UI that points to /openapi.json (no extra deps)."""
    return '''<!doctype html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Swagger UI — Simple API</title>
    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css"/>
  </head>
  <body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
    <script>
      window.onload = function() {
        SwaggerUIBundle({
          url: '/openapi.json',
          dom_id: '#swagger-ui',
          presets: [SwaggerUIBundle.presets.apis],
          layout: 'BaseLayout'
        });
      };
    </script>
  </body>
</html>'''


if __name__ == "__main__":
    # Démarre le serveur local. Ouvrez http://localhost:5000/docs pour Swagger UI
    app.run(host="127.0.0.1", port=5000, debug=True)
