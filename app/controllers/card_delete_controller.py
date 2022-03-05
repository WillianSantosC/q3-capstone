from http import HTTPStatus

from flask import current_app, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session

from app.models.card_model import CardModel


@jwt_required()
def delete_card(id):
    session: Session = current_app.db.session
    try:
        card: CardModel = CardModel().query.filter_by(id=id).first()
        session.delete(card)
        session.commit()
        return '', HTTPStatus.OK
    except:
        return {'msg': 'card not found'}, HTTPStatus.NOT_FOUND
