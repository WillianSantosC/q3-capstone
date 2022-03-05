from http import HTTPStatus

from flask import current_app, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session

from app.models.card_model import CardModel


@jwt_required()
def update_card(id):
    session: Session = current_app.db.session
    data = request.get_json()

    try:
        card: CardModel = CardModel().query.filter_by(id=id).first()
        card.title = data['title'].capitalize()
        card.description = data['description'].capitalize()

        session.add(card)
        session.commit()
        return '', HTTPStatus.OK

    except:
        return {'msg': 'activity not found'}, HTTPStatus.NOT_FOUND
