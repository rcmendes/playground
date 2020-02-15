from app import db
from models import Puppy


for i in range(1,11):
    p = Puppy(f"Puppy {i}")
    db.session.add(p)
db.session.commit()

list = Puppy.query.all()

for puppy in list:
    print(f"ID: {puppy.id} \t| Name: {puppy.name}")

# for puppy in list:
    # db.session.delete(puppy)
# db.session.commit()