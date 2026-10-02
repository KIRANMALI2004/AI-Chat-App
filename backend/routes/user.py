from flask import Blueprint, jsonify, request

from middleware.auth import login_required
from models.user import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/profile", methods=["GET"])
@login_required
def profile(current_user):

    return jsonify({
        "success": True,
        "user": {
            "id": str(current_user["_id"]),
            "name": current_user["name"],
            "email": current_user["email"],
            "avatar": current_user.get("avatar", "")
        }
    }), 200


@user_bp.route("/profile", methods=["PUT"])
@login_required
def update_profile(current_user):

    data = request.get_json()

    update_data = {
        "name": data.get("name"),
        "email": data.get("email")
    }

    User.update(str(current_user["_id"]), update_data)

    user = User.find_by_id(str(current_user["_id"]))

    return jsonify({
        "success": True,
        "message": "Profile Updated Successfully",
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "avatar": user.get("avatar", "")
        }
    }), 200