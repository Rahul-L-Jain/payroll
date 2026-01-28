from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
import mysql.connector
from app.config import Config

# Initialize Bcrypt
bcrypt = Bcrypt()

# Create blueprint
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# MySQL connection helper
def get_db_connection():
    return mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        port=Config.DB_PORT
    )

# Login route
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()

        if not row:
            return jsonify({"message": "User not found"}), 404

        # Check if user is active
        if not row.get("is_active", True):
            return jsonify({"message": "User inactive"}), 403

        # Verify password
        if not bcrypt.check_password_hash(row["password_hash"], password):
            return jsonify({"message": "Invalid credentials"}), 401

        # Login successful
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": row["id"],
                "email": row["email"],
                "role": row["role"]
            }
        }), 200

    except Exception as e:
        print("Login error:", e)
        return jsonify({"message": "Internal server error"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
