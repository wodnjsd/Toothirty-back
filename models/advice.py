from app import db
from models.base import BaseModel

class AdviceModel(db.Model, BaseModel):

  __tablename__ = "advice"

  content = db.Column(db.Text, nullable=False)
