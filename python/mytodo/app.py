import os

from flask import Flask
from flask_restful import Api, Resource
from datetime import datetime
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from db import db
from ma import ma
from resources.user import User
from resources.login import Login
from resources.task import Task

app = Flask(__name__)

# Setup database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")


@app.before_first_request
def create_database():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_schema_errors(err):
    return err.messages, 400


api = Api(app)

api.add_resource(User, "/users", "/users/<int:user_id>")
api.add_resource(Login, "/login")
api.add_resource(Task, "/tasks", "/tasks/<int:task_id>")

if "__main__" == __name__:
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
