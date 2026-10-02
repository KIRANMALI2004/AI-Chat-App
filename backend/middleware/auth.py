import jwt
from functools import wraps
from flask import request, jsonify, current_app
from models.user import User


def token_required(func):

    @wraps(func)
    def decorated(*args, **kwargs):

        token = None


        if "Authorization" in request.headers:

            auth_header = request.headers["Authorization"]

            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]


        if not token:
            return jsonify({
                "message": "Token is missing"
            }), 401


        try:

            data = jwt.decode(
                token,
                current_app.config["JWT_SECRET_KEY"],
                algorithms=["HS256"]
            )


            current_user = User.find_by_id(
    data["user_id"]
)

            if not current_user:
                return jsonify({
                    "message":"User not found"
                }),404


        except Exception as e:

            return jsonify({
                "message":"Invalid token",
                "error":str(e)
            }),401



        return func(
            current_user,
            *args,
            **kwargs
        )


    return decorated




login_required = token_required