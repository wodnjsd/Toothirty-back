from app import db

problem_advice = db.Table('problem_advice',
    db.Column('problem_id', db.Integer, db.ForeignKey('problems.id'), primary_key=True),
    db.Column('advice_id', db.Integer, db.ForeignKey('advice.id'), primary_key=True)
)