from curses.ascii import HT
from http import HTTPStatus

# ! import g
from flask import Blueprint, request, g
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route
from models.type import TypeModel
from models.problem import ProblemModel

from middleware.secure_route import secure_route
from serializers.problem import ProblemSchema
from serializers.type import TypeSchema

type_schema = TypeSchema()
problem_schema = ProblemSchema()

router = Blueprint("types", __name__)


@router.route("/all", methods=["GET"])
def get_types():
    types = TypeModel.query.all()

    return type_schema.jsonify(types, many=True), HTTPStatus.OK


@router.route("/types/<int:type_id>", methods=["GET"])
def get_single_type(type_id):

    type = TypeModel.query.get(type_id)

    if not type:
        return {"message": "Type not found"}, HTTPStatus.NOT_FOUND

    return type_schema.jsonify(type), HTTPStatus.OK


@router.route("/types", methods=["POST"])
@secure_route
def create_type():
    type_dictionary = request.json

    try:
        type = type_schema.load(type_dictionary)
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    # ! Add the current user
    type.user_id = g.current_user.id
    type.save()

    return type_schema.jsonify(type), HTTPStatus.CREATED




@router.route("/types/<int:type_id>", methods=["DELETE"])
@secure_route
def remove_type(type_id):
    type = TypeModel.query.get(type_id)

    if not type:
        return {"message": "Type not found"}, HTTPStatus.NOT_FOUND

    type.remove()

    return '', HTTPStatus.NO_CONTENT

