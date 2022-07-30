from app import db
from models.base import BaseModel

class AdviceModel(db.Model, BaseModel):

  __tablename__ = "advice"

  content = db.Column(db.Text, nullable=False)
  # user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)

  # user = db.relationship('UserModel', backref='advice_users')
  # problem = db.relationship('ProblemModel', backref='type_problems')