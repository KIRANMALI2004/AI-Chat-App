from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

class JWTService:

    @staticmethod
    def generate_tokens(user_id):

        access = create_access_token(identity=str(user_id))

        refresh = create_refresh_token(identity=str(user_id))

        return {

            "access_token": access,

            "refresh_token": refresh

        }