from flask import Blueprint, jsonify, request

bp = Blueprint("students", __name__)

students = []

@bp.route("/students", methods=["GET"])
def list_students():
    return jsonify(students), 200

@bp.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    students.append(data)
    return jsonify(data), 201
