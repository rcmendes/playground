from uuid import uuid4
from db import db

from models.base import BaseModel


class AgendaModel(BaseModel):
    __tablename__ = "agendas"

    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(2048), nullable=True)

    user_id = db.Column(db.String(36), db.ForeignKey(
        "users.id"), nullable=False)
    user = db.relationship("UserModel")
    tasks = db.relationship("TaskModel", lazy="dynamic")

    def __init__(self, user_id: str, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex
        self.user_id = user_id

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}, user_id: {self.user_id}"

    @classmethod
    def fetch_all(cls) -> ["AgendaModel"]:
        return cls.query.all()

    @classmethod
    def find_by_title(cls, title: str) -> "AgendaModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, id: str) -> "AgendaModel":
        return cls.query.filter_by(id=id).first()
