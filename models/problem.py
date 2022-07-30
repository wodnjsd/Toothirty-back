from app import db
from models.base import BaseModel
from models.user import UserModel


class ProblemModel(db.Model, BaseModel):

  __tablename__ = "problems"

  name = db.Column(db.Text, nullable=False, unique=True)
  
  