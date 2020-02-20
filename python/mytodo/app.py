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
from resources.login import Login
from resources.task import Task
from resources.agenda import Agenda

app = Flask(__name__)

# Setup database
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URI", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

api = Api(app)

# migrate = Migrate(app, db)


@app.before_first_request
def create_database():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_schema_errors(err):
    return err.messages, 400


api.add_resource(User, "/users", "/users/<int:user_id>")
api.add_resource(Login, "/login")
api.add_resource(Task, "/tasks", "/tasks/<int:task_id>")
api.add_resource(Agenda, "/agendas", "/agendas/<int:agenda_id>")

if "__main__" == __name__:
    db.init_app(app)
    ma.init_app(app)

    app.run(port=5000, debug=True)
