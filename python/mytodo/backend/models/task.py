from uuid import uuid4
from db import db

from models.base import BaseModel
from models.agenda import AgendaModel


class TaskModel(BaseModel):
    __tablename__ = "tasks"

    title = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.String(1024), nullable=True)

    agenda_id = db.Column(db.String(36), db.ForeignKey(
        "agendas.id"), nullable=False)
    agenda = db.relationship("AgendaModel")

    def __init__(self, title: str, agenda_id: str, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex
        self.title = title
        self.agenda_id = agenda_id

    @classmethod
    def fetch_all(cls) -> ["TaskModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, task_id: str) -> "TaskModel":
        return cls.query.filter_by(id=task_id).first()
