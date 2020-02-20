import os

from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
import bcrypt

from schemas.user import register_user_request, register_user_response, user_response, users_response
from models.user import UserModel

salt = os.getenv("USER_PASSWORD_SALT").encode()


class User(Resource):
    @classmethod
    def get(cls, user_id: str = None):
        if not user_id:
            return users_response.dump(UserModel.fetch_all()), 200

        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404

        return user_response.dump(user)

    @classmethod
    @jwt_required
    def post(cls):
        user_json = request.get_json()
        userSchema = register_user_request.load(user_json)

        if UserModel.find_by_username(userSchema["username"]):
            return {"message": "Username already exists"}, 400

        user = UserModel(**userSchema)
        hash = bcrypt.hashpw(user.password.encode('utf8'), salt)
        print(hash)
        return {}, 200
        user.password = bcrypt.hashpw(
            user.password.encode('utf8'), bcrypt.gensalt(10))

        return user, 200
        user.save()

        return register_user_response.dump(user), 201
