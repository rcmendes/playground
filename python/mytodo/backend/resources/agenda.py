from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from models.agenda import AgendaModel
from models.user import UserModel
from schemas.agenda import agendaSchema, agendaListSchema


class Agenda(Resource):
    @classmethod
    @jwt_required
    def get(cls, agenda_id: str = None):
        if not agenda_id:
            list = AgendaModel.fetch_all()
            return agendaListSchema.dump(list), 200
        agenda = AgendaModel.find_by_id(agenda_id)
        if not agenda:
            return {"message": "Agenda <id={}> not found.".format(agenda_id)}, 404

        return agendaSchema.dump(agenda), 200

    @classmethod
    @jwt_required
    def post(cls):
        agenda_json = request.get_json()
        agenda = agendaSchema.load(agenda_json)

        if not UserModel.find_by_id(agenda.user_id):
            return {"message": "The specified user <id={agenda.user_id}> was not found."}, 400

        if AgendaModel.find_by_title(agenda.title):
            return {"message": "This title is already been used."}, 400

        agenda.save()

        return agendaSchema.dump(agenda), 201
