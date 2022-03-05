from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.card_model import CardModel


@jwt_required()
def get_card(id):
    card: CardModel = CardModel().query.filter_by(id=id).first()

    if card != None:
        return jsonify(card), HTTPStatus.OK

    else:
        return {'msg': 'card not found'}, HTTPStatus.NOT_FOUND
