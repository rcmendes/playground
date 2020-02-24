import bcrypt
from flask import request, jsonify
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token

from models.user import UserModel


class Login(Resource):
    @classmethod
    def post(cls):
        if not request.is_json:
            return jsonify({"message": "Missing JSON in request"}), 400

        email = request.json.get('email', None)
        password = request.json.get('password', None)
        if not email:
            return jsonify({"message": "Missing e-mail parameter"}), 400
        if not password:
            return jsonify({"message": "Missing password parameter"}), 400

        user = UserModel.find_by_email(email)
        if not user:
            return {"message": "User credentials (email/password) are incorrect."}, 401

        if not bcrypt.checkpw(password.encode('utf8'), user.password):
            return {"message": "User credentials (email/password) are incorrect."}, 401

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200
