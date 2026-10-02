import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    MONGO_URI = os.getenv("MONGO_URI")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

    MAX_CONTENT_LENGTH = int(
        os.getenv("MAX_CONTENT_LENGTH", 16777216)
    )
    
    EMAIL = os.getenv("EMAIL")
    
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")