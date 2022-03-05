from email.policy import HTTP
from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Query, Session
from app.models.activity_model import ActivityModel

from app.models.card_model import CardModel
from app.models.user_model import UserModel

@jwt_required()
def create_card(activity_id):
    session: Session = current_app.db.session
    activity_query: Query = ActivityModel.query
    card_query: Query = CardModel.query
    user_query: Query = UserModel.query

    data: dict = request.get_json()
    title = data['title']
    description = data['description']

    email = get_jwt_identity().get('email')
    user: UserModel = user_query.filter_by(email=email).first()


    new_card = CardModel(title=title, description=description)
    new_card.activity_id = activity_id
    new_card.user_id = user.id

    
    session.add(new_card)
    session.commit()

    return jsonify(new_card), HTTPStatus.CREATED



    