from flask_restful import Resource
from datetime import datetime


class Ping(Resource):
    @classmethod
    def get(cls):
        return {"message": datetime.utcnow().isoformat()}, 200
