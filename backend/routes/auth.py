from flask import Blueprint, request, jsonify, current_app
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({
            "message": "All fields are required"
        }), 400

    existing_user = User.find_by_email(email)

    if existing_user:
        return jsonify({
            "message": "User already exists"
        }), 400

    hashed_password = generate_password_hash(password)

    User.create({
        "name": username,
        "email": email,
        "password": hashed_password
    })

    return jsonify({
        "message": "Registration Successful"
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.find_by_email(email)

    if not user:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    if not check_password_hash(user["password"], password):
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    token = jwt.encode(
        {
            "user_id": str(user["_id"]),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
        },
        current_app.config["JWT_SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({
        "token": token,
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        }
    }), 200