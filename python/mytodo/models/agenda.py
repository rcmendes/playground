from uuid import uuid4
from db import db


class Agenda(db.Model):
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
        self.user_id = user_id
        self.id = uuid4()

    # Create Agenda Schema from Marshmallow-SQLAlchemy
