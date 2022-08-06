from app import ma
from models.type import TypeModel
from marshmallow import fields


class TypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TypeModel
        load_instance = True

    problems = fields.Nested("ProblemSchema", many=True)
    user = fields.Nested("UserSchema", many=False)
