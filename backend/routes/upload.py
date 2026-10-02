import os
from flask import Blueprint, request, jsonify, current_app
from sqlalchemy import text
from werkzeug.utils import secure_filename
from services.file_reader import read_file

upload_bp = Blueprint("upload", __name__)

last_uploaded_text = ""


@upload_bp.route("/", methods=["POST"])
def upload_file():
    global last_uploaded_text

    print("Upload API Called")

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "message": "No file selected"
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "Empty filename"
        }), 400

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)
    
    text  = read_file(filepath)
    return jsonify({
        "success": True,
        "filename": filename,
        "text": text
        
    })