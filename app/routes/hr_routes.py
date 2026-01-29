from flask import Blueprint, jsonify

hr_bp = Blueprint("hr", __name__, url_prefix="/hr")

@hr_bp.route("/dashboard", methods=["GET"])
def hr_dashboard():
    return jsonify({
        "message": "HR dashboard working"
    })


