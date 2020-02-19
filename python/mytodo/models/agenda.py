from uuid import uuid4
from db import db

from models.task import TaskModel
from models.user import UserModel


class AgendaModel(db.Model):
    __tablename__ = "agendas"

    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(2048), nullable=False)

    user_id = db.Column(db.String(36), db.ForeignKey(
        "users.id"), nullable=False)
    user = db.relationship("UserModel")
    tasks = db.relationship("TaskModel", lazy="dinamic")

    def __init__(self, user_id: str, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex
        self.user_id = user_id

    # Create Agenda Schema from Marshmallow-SQLAlchemy
