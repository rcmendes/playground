from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nulable=False, unique=True)
    password = db.Column(db.String(255), nulable=False)

    @classmethod
    def find_by_username(cls, username: str):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id: int):
        return cls.query.filter_by(id=id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_into_db(self):
        db.session.add(self)
        db.session.commit()
