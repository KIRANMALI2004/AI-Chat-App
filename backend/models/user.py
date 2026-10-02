from datetime import datetime
from bson import ObjectId
from database.mongo import users


class User:

    @staticmethod
    def create(data):

        user = {
            "name": data["name"],
            "email": data["email"],
            "password": data["password"],
            "avatar": "",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        result = users.insert_one(user)

        return str(result.inserted_id)

    @staticmethod
    def find_by_email(email):

        return users.find_one({
            "email": email
        })

    @staticmethod
    def find_by_id(user_id):

        return users.find_one({
            "_id": ObjectId(user_id)
        })

    @staticmethod
    def update(user_id, data):

        data["updated_at"] = datetime.utcnow()

        users.update_one(
            {
                "_id": ObjectId(user_id)
            },
            {
                "$set": data
            }
        )

    @staticmethod
    def delete(user_id):

        users.delete_one({
            "_id": ObjectId(user_id)
        })