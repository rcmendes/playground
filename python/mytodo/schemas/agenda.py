from ma import ma
from marshmallow import pre_dump, post_dump

from models.agenda import AgendaModel


class AgendaSchema(ma.ModelSchema):
    class Meta:
        model = AgendaModel
        load_only = ("tasks", "user",)
        dump_only = ("id",)
        include_fk = True

    @post_dump(pass_many=False)
    def remove_fiels_with_value_as_none(self, data, many, **kwargs):
        """Remove all key that the value is missing."""

        data = {k: v for k, v in data.items() if v}
        return data


agendaSchema = AgendaSchema()
agendaListSchema = AgendaSchema(many=True)
