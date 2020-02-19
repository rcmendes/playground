from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    # description = db.Column(db.String(1024), nullable=True)

    # def __init__(self, title: str, **kwargs):
    #     super().__init__(**kwargs)
    #     self.title = title

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, task_id: int):
        return cls.query.filter_by(id=task_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
