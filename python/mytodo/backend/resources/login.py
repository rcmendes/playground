import bcrypt

from flask import request, jsonify
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token, create_refresh_token

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
