from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/mydb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  age = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
  person = Person.query.first()
  return 'Hello ' + person.name