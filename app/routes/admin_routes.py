from flask import Blueprint, jsonify

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/dashboard", methods=["GET"])
def admin_dashboard():
    return jsonify({
        "message": "Admin dashboard working"
    })

