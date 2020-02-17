import os
from flask import Flask
from flask_restful import Api, Resource
from datetime import datetime
from db import db
from ma import ma
from resources.user import User
from resources.login import Login
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

app = Flask(__name__)


# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir}/data.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!


@app.before_first_request
def create_database():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_schema_errors(err):
    return err.messages, 400


api = Api(app)

api.add_resource(User, "/users", "/users/<user_id>")
api.add_resource(Login, "/login")

if "__main__" == __name__:
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
