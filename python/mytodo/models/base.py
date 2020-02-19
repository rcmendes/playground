from uuid import uuid4
from db import db


class BaseModel(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.Data)
    archived_at = db.Column()
    update_at = db.Column()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        id = uuid4().hex
