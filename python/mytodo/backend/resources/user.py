import os

from flask_restful import Resource, request
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
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if UserModel.find_by_email(user.email):
            return {"message": "E-mail already exists"}, 400

        hash = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt(10))
        user.password = hash

        user.save()

        return user_schema.dump(user), 201

    @classmethod
    def patch(cls, user_id: str):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)

        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": f"User <id={user_id} not found."}, 404

        if user_data.email != user.email and UserModel.find_by_email(user_data.email):
            return {"message": "E-mail already exists"}, 400
        else:
            user.email = user_data.email

        if user_data.password:
            hash = bcrypt.hashpw(user_data.password.encode(
                'utf8'), bcrypt.gensalt(10))
            user.password = hash

        user.save()

        return user_schema.dump(user), 204

    @classmethod
    def put(cls, user_id: str):
        user_json = request.get_json()
        updated_user = user_schema.load(user_json)

        old_user = UserModel.find_by_id(user_id)
        if not old_user:
            return {"message": f"User <id={user_id} not found."}, 404

        if updated_user.email != old_user.email and UserModel.find_by_email(updated_user.email):
            return {"message": "E-mail already exists"}, 400

        hash = bcrypt.hashpw(updated_user.password.encode(
            'utf8'), bcrypt.gensalt(10))
        updated_user.password = hash

        updated_user.id = user_id
        updated_user.save()

        return user_schema.dump(updated_user), 200
