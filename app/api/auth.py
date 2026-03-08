from flask import Blueprint, request, jsonify

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if data["username"] == "admin" and data["password"] == "password":
        return jsonify({"message": "login successful"}), 200

    return jsonify({"message": "invalid credentials"}), 401


