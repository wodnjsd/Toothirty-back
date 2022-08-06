from app import ma
from models.advice import AdviceModel


class AdviceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdviceModel
        load_instance = True
