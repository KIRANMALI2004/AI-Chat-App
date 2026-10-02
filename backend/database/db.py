from database.mongo import (
    db,
    users,
    chats,
    messages,
    files
)
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Database:

    @staticmethod
    def get_db():
        return db

    @staticmethod
    def users():
        return users

    @staticmethod
    def chats():
        return chats

    @staticmethod
    def messages():
        return messages

    @staticmethod
    def files():
        return files