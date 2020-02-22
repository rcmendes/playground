import os

from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
import bcrypt

from schemas.user import user_schema, user_list_schema
from models.user import UserModel


class User(Resource):
    @classmethod
    def get(cls, user_id: str = None):
        if not user_id:
            return user_list_schema.dump(UserModel.fetch_all()), 200

        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404

        return user_schema.dump(user)

    @classmethod
    @jwt_required
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_username(user.username):
            return {"message": "Username already exists"}, 400

        hash = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt(10))
        user.password = hash

        user.save()

        return user_schema.dump(user), 201
