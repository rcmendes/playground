from ma import ma

from models.agenda import AgendaModel


class AgendaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AgendaModel
        load_only = ("tasks", "description")
        dump_only = ("id")
        include_fk = True
        load_instance = True


agendaSchema = AgendaSchema()
agendaListSchema = AgendaSchema(many=True)
