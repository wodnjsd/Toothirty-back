from app import db
from models.base import BaseModel
from models.problem import ProblemModel

class TypeModel(db.Model, BaseModel):

  __tablename__ = "types"

  name = db.Column(db.Text, nullable=False, unique=True)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
  image = db.Column(db.Text, nullable=True)


  user = db.relationship('UserModel', backref='advice_users')
  problems = db.relationship('ProblemModel', backref='problems', cascade="all, delete")