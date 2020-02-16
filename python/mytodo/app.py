from flask import Flask
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)


class Ping(Resource):
    @classmethod
    def get(cls):
        return {"Ping": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}


api.add_resource(Ping, "/")

if "__main__" == __name__:
    app.run(port=5000, debug=True)
