from datetime import datetime
from bson import ObjectId
from database.mongo import files


class File:

    @staticmethod
    def save(user_id, filename, path):

        document = {

            "user_id": ObjectId(user_id),

            "filename": filename,

            "path": path,

            "created_at": datetime.utcnow()

        }

        result = files.insert_one(document)

        return str(result.inserted_id)

    @staticmethod
    def get_all(user_id):

        return list(

            files.find(

                {

                    "user_id": ObjectId(user_id)

                }

            )

        )

    @staticmethod
    def delete(file_id):

        files.delete_one(

            {

                "_id": ObjectId(file_id)

            }

        )