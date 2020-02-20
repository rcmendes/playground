from flask_restful import Resource, request
from schemas.user import register_user_request, register_user_response, user_response, users_response
from marshmallow import ValidationError
from models.user import UserModel
from flask_jwt_extended import jwt_required


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

        user.save()

        return register_user_response.dump(user), 201
