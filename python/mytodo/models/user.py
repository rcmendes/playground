from uuid import uuid4
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), nullable=False,
                         unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username: str, password: str, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username: str):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id: int):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
