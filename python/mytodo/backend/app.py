import os

from datetime import datetime

from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
# from flask_migrate import Migrate
from marshmallow import ValidationError

from db import db
from ma import ma
from resources.user import User
from resources.login import Login, RefreshToken
from resources.task import Task
from resources.agenda import Agenda
from resources.task import Task


app = Flask(__name__)

app.config.from_object("config")

jwt = JWTManager(app)

api = Api(app)

# migrate = Migrate(app, db)


@app.before_first_request
def create_database():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_schema_errors(err):
    return err.messages, 400


api.add_resource(User, "/users", "/users/<string:user_id>")
api.add_resource(Login, "/login")
api.add_resource(Task, "/tasks", "/tasks/<string:task_id>")
api.add_resource(Agenda, "/agendas", "/agendas/<string:agenda_id>")
api.add_resource(RefreshToken, "/refresh")

if "__main__" == __name__:
    db.init_app(app)
    ma.init_app(app)

    app.run(port=5000, debug=True)
