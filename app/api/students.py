from flask import Blueprint, jsonify, request

bp = Blueprint("students", __name__)

students = []

@bp.route("/students", methods=["GET"])
def list_students():
    return jsonify(students)

@bp.route("/students", methods=["POST"])
def create_student():
    data = request.json
    students.append(data)
    return jsonify(data), 201

@bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    if id < len(students):
        return jsonify(students[id])
    return {"error": "Not found"}, 404

@bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json
    if id < len(students):
        students[id] = data
        return jsonify(data)
    return {"error": "Not found"}, 404

@bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    if id < len(students):
        students.pop(id)
        return {}, 204
    return {"error": "Not found"}, 404
