from app import db
# from models.base import BaseModel

# class ProblemAdviceModel(db.Model, BaseModel):

#   __tablename__ = "problem_advice"

#   problem_id = db.Column(db.Integer, db.ForeignKey("problems.id"))
#   advice_id = db.Column(db.Integer, db.ForeignKey("advice.id"))


problem_advice = db.Table('problem_advice',
    db.Column('problem_id', db.Integer, db.ForeignKey('problems.id'), primary_key=True),
    db.Column('advice_id', db.Integer, db.ForeignKey('advice.id'), primary_key=True)
)

# problem = db.relationship("ProblemModel", back_populates="advice")
# advice = db.relationship("AdviceModel", back_populates="problems")