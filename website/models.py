from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
  username = db.Column(db.String(12), unique=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  last_name = db.Column(db.String(150))
  
  
