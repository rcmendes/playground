from flask_restful import Resource


class UserResource(Resource):
    @classmethod
    def get(cls, id: str):
        return {"id": "12345"}

