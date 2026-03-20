#!/usr/bin/python3


from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    u = users.get(username)
    return u and check_password_hash(u['password'], password)


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    if not data or not all(k in data for k in ("username", "password")):
        return jsonify({"error": "Missing credentials"}), 401
    user = users.get(data["username"])
    if not user or not check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    identity = {
        "username": user["username"],
        "role": user["role"],
    }
    token = create_access_token(identity=identity)
    return jsonify({"access_token": token}), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    identity = get_jwt_identity() or {}
    if identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def needs_fresh(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
