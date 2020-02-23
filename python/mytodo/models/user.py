from uuid import uuid4

from db import db
from models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    email = db.Column(db.String(100), nullable=False,
                      unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email: str, password: str, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex
        self.email = email
        self.password = password

    @classmethod
    def fetch_all(cls) -> ["UserModel"]:
        return cls.query.all()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id: str) -> "UserModel":
        return cls.query.filter_by(id=id).first()
