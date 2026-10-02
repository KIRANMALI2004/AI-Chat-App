from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)

db = client.ai_chat_app

users = db.users

chats = db.chats

messages = db.messages

files = db.files