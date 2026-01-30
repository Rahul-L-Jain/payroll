from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required

employee_bp = Blueprint("employee", __name__, url_prefix="/employee")

@employee_bp.route("/dashboard")
@role_required("employee")
def employee_dashboard():
    return jsonify({"message": "Welcome Employee"})

