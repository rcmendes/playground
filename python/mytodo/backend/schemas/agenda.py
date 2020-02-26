from schemas.base import BaseSchema
from models.agenda import AgendaModel


class AgendaSchema(BaseSchema):
    class Meta:
        model = AgendaModel
        load_only = ("tasks", "user",)
        dump_only = ("id",)
        include_fk = True


agendaSchema = AgendaSchema()
agendaListSchema = AgendaSchema(many=True)
