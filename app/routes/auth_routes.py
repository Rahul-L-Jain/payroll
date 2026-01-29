from flask import Blueprint, request, jsonify
from app import bcrypt

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    return jsonify({
        "message": "Login endpoint reachable",
        "data": data
    })

