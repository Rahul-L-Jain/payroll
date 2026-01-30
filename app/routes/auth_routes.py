from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.extensions import bcrypt
import mysql.connector
from mysql.connector import Error
from app.config import Config

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

def get_db():
    return mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )

# ---------------- REGISTER ----------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "user")

    if not email or not password:
        return {"message": "Email and password required"}, 400

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")

    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (email, password_hash, role) VALUES (%s, %s, %s)",
            (email, hashed, role)
        )
        db.commit()
    except Error as e:
        if e.errno == 1062:
            return {"message": "User already exists"}, 409
        return {"message": "Database error"}, 500
    finally:
        cursor.close()
        db.close()

    return {"message": "User registered successfully"}, 201


# ---------------- LOGIN (JWT) ----------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    access_token = create_access_token(identity=user["id"])

    if not email or not password:
        return {"message": "Email and password required"}, 400

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, email, password_hash, role FROM users WHERE email=%s",
        (email,)
    )
    user = cursor.fetchone()

    cursor.close()
    db.close()

    if not user:
        return {"message": "Invalid credentials"}, 401

    if not bcrypt.check_password_hash(user["password_hash"], password):
        return {"message": "Invalid credentials"}, 401

    # ✅ CREATE JWT
    access_token = create_access_token(
        identity={
            "id": user["id"],
            "email": user["email"],
            "role": user["role"]
        }
    )

    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "user": {
            "id": user["id"],
            "email": user["email"],
            "role": user["role"]
        }
    }), 200


# ---------------- HEALTH CHECK ----------------
@auth_bp.route("/ping")
def ping():
    return {"message": "auth works"}

