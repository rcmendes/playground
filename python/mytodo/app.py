from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] =

api = Api(app)

if "__main__" == __name__:
    app.run(port=5000, debug=True)
