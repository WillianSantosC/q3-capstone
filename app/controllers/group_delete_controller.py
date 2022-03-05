from http import HTTPStatus

from flask import current_app, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import DataError
from sqlalchemy.orm import Query, Session

from app.models.group_model import GroupModel 
from app.models.user_model import UserModel


@jwt_required()
def delete_group(group_id: str):
    session: Session = current_app.db.session
    user_query: Query = UserModel.query
    group_query: Query = GroupModel.query

    email = get_jwt_identity().get('email')

    user: UserModel = user_query.filter_by(email=email).first()

    try:
        group: GroupModel = group_query.get(group_id)

        if group.owner_id == user.id:
            session.delete(group)
            session.commit()
            return '', HTTPStatus.NO_CONTENT
        else:
            return jsonify(error='Permission denied'), HTTPStatus.FORBIDDEN
    except DataError:
        return jsonify(error='Group not found'), HTTPStatus.NOT_FOUND
