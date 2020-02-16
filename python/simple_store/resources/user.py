from flask_restful import Resource, reqparse
from models.user import UserModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username", type=str, required=True, help="This field cannot be blank."
)
_user_parser.add_argument(
    "password", type=str, required=True, help="This field cannot be blank."
)


class UserRegisterAndList(Resource):
    @classmethod
    def post(cls):
        data = _user_parser.parse_args()

        username = data["username"]
        if UserModel.find_by_username(username):
            return {"message": "This username is already been used."}

        user = UserModel(**data)
        user.save()
        return {"message": "User created successfully.",
                "data": user.to_json()}, 201

    @classmethod
    def get(cls):
        user_list = UserModel.fetch_all()

        return [user.to_json() for user in user_list], 200


class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404

        return user.to_json(), 200


# class UserList(Resource):
    # @classmethod
    # def get(cls):
    #     user_list = UserModel.fetch_all()

    #     return [user.to_json() for user in user_list], 200
