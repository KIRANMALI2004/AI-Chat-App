from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from routes.auth import auth_bp
from routes.user import user_bp
from routes.chat import chat_bp
from routes.file import file_bp
from routes.upload import upload_bp
from services.email_service import send_email
import os
app = Flask(__name__)

app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
app.config["MAX_CONTENT_LENGTH"] = Config.MAX_CONTENT_LENGTH
app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
CORS(
    app,
    resources={r"/api/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True,
    )

jwt = JWTManager(app)
# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(chat_bp, url_prefix="/api/chat")
app.register_blueprint(file_bp, url_prefix="/api/file")
app.register_blueprint(upload_bp, url_prefix="/api/upload")
@app.route("/")
def home():

    return {
        "status": "success",
        "message": "AI Chat Backend Running",
        "version": "1.0.0"
    }


@app.route("/health")
def health():

    return {
        "status": "healthy"
    }

@app.route("/test-email")
def test_email():

    ok = send_email(
        "your_email@gmail.com",
        "AI Chat App",
        "Hello from Flask!"
    )

    return {
        "success": ok
    }

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )