from app import ma
from models.problem import ProblemModel
from marshmallow import fields


class ProblemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProblemModel
        load_instance = True

    advice = fields.Nested("AdviceSchema", many=True)
    type = fields.Nested("TypeSchema", many=True)
    user = fields.Nested("UserSchema", many=False)