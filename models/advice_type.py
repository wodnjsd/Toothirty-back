from app import db

problem_advice = db.Table('problem_advice',
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'), primary_key=True),
    db.Column('advice', db.Integer, db.ForeignKey('advice.id'), primary_key=True)
)