import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import Puppy

app = Flask(__name__)

app.config["SECRET_KEY"] = "mys3cr3tk3y"

# DATABASE SETUP
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)
#####

### MODELS
class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.id:
            return f"ID: {self.id}\t| Name: {self.name}"
        else:
            return f"Name: {self.name}"
#####

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register_puppy():
    return render_template("register_puppy.html")


@app.route("/list")
def list_puppy():
    puppies = Puppy.query.all()
    return render_template('list_puppy.html', puppies=puppies)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
