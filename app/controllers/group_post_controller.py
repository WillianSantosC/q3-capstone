from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Query, Session

from app.models.group_model import GroupModel
from app.models.user_model import UserModel


@jwt_required()
def create_group():
    session: Session = current_app.db.session
    user_query: Query = UserModel.query
    data: dict = request.get_json()

    email = get_jwt_identity().get('email')

    user: UserModel = user_query.filter_by(email=email).first()

    new_group: GroupModel = GroupModel(title=data.get('title'))

    user.groups.append(new_group)

    session.add(new_group)
    session.commit()

    return jsonify(new_group), HTTPStatus.CREATED
