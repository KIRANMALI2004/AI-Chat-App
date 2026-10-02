from datetime import datetime
from bson import ObjectId
from database.mongo import chats


class Chat:

    @staticmethod
    def create(user_id, title):

        chat = {

            "user_id": ObjectId(user_id),

            "title": title,

            "model": "gpt-4o-mini",

            "created_at": datetime.utcnow(),

            "updated_at": datetime.utcnow()

        }

        result = chats.insert_one(chat)

        return str(result.inserted_id)

    @staticmethod
    def get_all(user_id):

        return list(

            chats.find(

                {

                    "user_id": ObjectId(user_id)

                }

            ).sort(

                "updated_at",

                -1

            )

        )

    @staticmethod
    def get(chat_id):

        return chats.find_one(

            {

                "_id": ObjectId(chat_id)

            }

        )

    @staticmethod
    def delete(chat_id):

        chats.delete_one(

            {

                "_id": ObjectId(chat_id)

            }

        )