from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

# client = MongoClient("mongodb://db:27017")
client = MongoClient("mongodb://localhost:27017")
db = client.bankAPI
users = db["users"]


def userExist(username):
    return users.find({"username": username}).count() != 0


def verifyPassword(username, password):
    if not userExist(username):
        return False

    hashed_password = users.find({"username": username})[0]["password"]

    return bcrypt.hashpw(password.encode('utf8'), hashed_password) == hashed_password


def responseJson(status, message):
    return {
        "status": status,
        "message": message
    }, status


class Account(Resource):
    def get(self):
        user_list_cursor = users.find()
        user_list = []
        for user in user_list_cursor:
            id = user["_id"]
            user["id"] = str(id)
            user.pop("_id")
            # user["password"] = user["password"].decode('utf8')
            user.pop("password")
            user_list.append(user)
        return responseJson(200, user_list)

    def post(self):
        data = request.get_json()

        username = data["username"]
        password = data["password"]

        if userExist(username):
            return responseJson(400, "Invalid username")

        hashed_password = bcrypt.hashpw(
            password.encode('utf8'), bcrypt.gensalt())

        user = {
            "username": username,
            "password": hashed_password,
            "balance": 0.0
        }

        new_user = users.insert_one(user)
        user["id"] = str(user["_id"])
        user.pop("password")
        user.pop("_id")

        return responseJson(201, user)


api.add_resource(Account, "/accounts")

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
