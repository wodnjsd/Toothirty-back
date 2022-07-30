from app import db
from models.base import BaseModel

class TypeModel(db.Model, BaseModel):

  __tablename__ = "types"

  name = db.Column(db.Text, nullable=False, unique=True)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)


  user = db.relationship('UserModel', backref='advice_users')
  # problem = db.relationship('ProblemModel', backref='problems', cascade="all, delete")