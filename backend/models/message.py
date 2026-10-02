from datetime import datetime
from bson import ObjectId
from database.mongo import messages


class Message:

    @staticmethod
    def create(chat_id, role, content):

        message = {

            "chat_id": ObjectId(chat_id),

            "role": role,

            "content": content,

            "created_at": datetime.utcnow()

        }

        result = messages.insert_one(message)

        return str(result.inserted_id)

    @staticmethod
    def get_messages(chat_id):

        return list(

            messages.find(

                {

                    "chat_id": ObjectId(chat_id)

                }

            ).sort(

                "created_at",

                1

            )

        )

    @staticmethod
    def delete(chat_id):

        messages.delete_many(

            {

                "chat_id": ObjectId(chat_id)

            }

        )