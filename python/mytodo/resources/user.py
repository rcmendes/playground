from flask_restful import Resource, request
from schemas.user import RegisterUserDTORequest, RegisterUserDTOResponse
from marshmallow import ValidationError
from models.user import UserModel
from flask_jwt_extended import jwt_required


class User(Resource):
    @classmethod
    def get(cls, user_id: int = None):
        if not user_id:
            respDTO = RegisterUserDTOResponse(many=True)
            return respDTO.dump(UserModel.fetch_all()), 200

        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404

        return RegisterUserDTOResponse().dump(user)

    @classmethod
    @jwt_required
    def post(cls):
        reqDTO = RegisterUserDTORequest()

        user_json = request.get_json()
        try:
            userSchema = reqDTO.load(user_json)

            if UserModel.find_by_username(userSchema["username"]):
                return {"message": "Username already exists"}, 400
            user = UserModel(**userSchema)

            user.save()
            return RegisterUserDTOResponse().dump(user), 201
        except ValidationError as err:
            return err.messages, 400

        return reqDTO.dump(user), 201
