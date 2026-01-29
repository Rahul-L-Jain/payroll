from flask import Blueprint, jsonify

employee_bp = Blueprint("employee", __name__, url_prefix="/employee")

@employee_bp.route("/dashboard", methods=["GET"])
def employee_dashboard():
    return jsonify({
        "message": "Employee dashboard working"
    })

