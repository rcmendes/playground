from db import db


class Agenda(db.Model):
    __tablename__ = "agendas"

    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(2048), nullable=False)

    user_id = db.

    # Create relationship with tasks and user
    # Create relationship between task and agenda
    # Replace all ID Integer by ID UUID
    # Create Agenda Schema from Marshmallow-SQLAlchemy
