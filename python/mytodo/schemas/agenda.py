from ma import ma
from models.agenda import Agenda


class Agenda(ma.ModelSchema):
    class Meta:
        model = Agenda
