from flask import Blueprint, request, jsonify
from middleware.auth import token_required
from database.db import db
from models.file import File
import os
from werkzeug.utils import secure_filename


file_bp = Blueprint("file", __name__)


UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@file_bp.route("/upload", methods=["POST"])
@token_required
def upload_file(current_user):

    if "file" not in request.files:
        return jsonify({
            "message": "No file uploaded"
        }), 400


    uploaded_file = request.files["file"]


    if uploaded_file.filename == "":
        return jsonify({
            "message": "No selected file"
        }), 400


    filename = secure_filename(uploaded_file.filename)

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )


    uploaded_file.save(filepath)


    new_file = File(
        filename=filename,
        filepath=filepath,
        user_id=current_user.id
    )


    db.session.add(new_file)
    db.session.commit()


    return jsonify({
        "message": "File uploaded successfully",
        "filename": filename
    }), 201



@file_bp.route("/list", methods=["GET"])
@token_required
def get_files(current_user):

    files = File.query.filter_by(
        user_id=current_user.id
    ).all()


    result = []

    for file in files:
        result.append({
            "id": file.id,
            "filename": file.filename,
            "filepath": file.filepath
        })


    return jsonify(result), 200