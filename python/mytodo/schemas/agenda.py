from ma import ma

from models.agenda import AgendaModel


class AgendaSchema(ma.ModelSchema):
    class Meta:
        model = AgendaModel
        load_only = ("tasks", "description", "user",)
        dump_only = ("id",)
        include_fk = True


agendaSchema = AgendaSchema()
agendaListSchema = AgendaSchema(many=True)
