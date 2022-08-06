from http import HTTPStatus
from flask import Blueprint, request, g
from models.advice import AdviceModel
from marshmallow.exceptions import ValidationError
from serializers.advice import AdviceSchema
from middleware.secure_route import secure_route

advice_schema = AdviceSchema()

router = Blueprint("advice", __name__)

#GET ADVICE
@router.route("/advice/<int:advice_id>", methods=["GET"])
def get_single_advice(advice_id):

    advice = AdviceModel.query.get(advice_id)

    if not advice:
        return {"message": "Advice not found"}, HTTPStatus.NOT_FOUND

    return advice_schema.jsonify(advice), HTTPStatus.OK

#CREATE ADVICE
@router.route("/advice", methods=["POST"])
def create_advice():
    advice_dictionary = request.json

    try:
        advice = advice_schema.load(advice_dictionary)
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}

    advice.save()

    return advice_schema.jsonify(advice)

#EDIT ADVICE
@router.route("/advice/<int:advice_id>", methods=["PUT"])
@secure_route
def update_advice(advice_id):
    advice_dictionary = request.json
    existing_advice = AdviceModel.query.get(advice_id)

    if not existing_advice:
        return {"message": "Advice not found"}, HTTPStatus.NOT_FOUND

    # ! Add this check whenever we want to make sure the tea is the user's tea that they're trying to update/delete
    if not g.current_user.id == existing_advice.user_id:
        return {"message": "Not your tea!"}, HTTPStatus.UNAUTHORIZED

    try:
        advice = advice_schema.load(advice_dictionary, instance=existing_advice, partial=True)

    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}

    advice.save()

    return advice_schema.jsonify(advice), HTTPStatus.OK

#DELETE ADVICE
@router.route("/advice/<int:advice_id>", methods=["DELETE"])
def remove_advice(advice_id):
    advice = AdviceModel.query.get(advice_id)

    if not advice:
        return {"message": "Advice not found"}, HTTPStatus.NOT_FOUND

    advice.remove()

    return '', HTTPStatus.NO_CONTENT

