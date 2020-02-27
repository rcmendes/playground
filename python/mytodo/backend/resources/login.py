import bcrypt

from flask import request, jsonify
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

from models.user import UserModel
from schemas.login import login_schema


class Login(Resource):
    @classmethod
    def post(cls):
        login = login_schema.load(request.get_json())

        email = login["email"]
        password = login["password"]

        user = UserModel.find_by_email(email)
        if not user:
            return {"message": "User credentials (email/password) are incorrect."}, 401

        if not bcrypt.checkpw(password.encode('utf8'), user.password):
            return {"message": "User credentials (email/password) are incorrect."}, 401

        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(identity=user.id)

        response = {"access_token": access_token,
                    "refresh_token": refresh_token}
        return response, 200


class RefreshToken(Resource):
    @classmethod
    @jwt_refresh_token_required
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        response = {'access_token': new_token}

        return response, 200
