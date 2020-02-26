from datetime import datetime
from uuid import uuid4

from db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    archived_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid4().hex
        timestamp = datetime.utcnow()
        self.created_at = timestamp
        # self.updated_at = timestamp

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def archive(self) -> None:
        timestamp = datetime.utcnow()
        self.updated_at = timestamp
        self.archived_at = timestamp

        db.session.add(self)
        db.session.commit()

    def save(self) -> None:
        if not self.updated_at:
            self.updated_at = self.created_at
        else:
            self .updated_at = datetime.utcnow()

        db.session.add(self)
        db.session.commit()

    def query(self):
