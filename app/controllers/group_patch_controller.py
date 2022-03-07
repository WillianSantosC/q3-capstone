from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.orm import Query, Session

from app.models.group_model import GroupModel
from app.models.user_model import UserModel


@jwt_required()
def update_group(group_id: str):
    session: Session = current_app.db.session
    user_query: Query = UserModel.query
    group_query: Query = GroupModel.query
    data: dict = request.get_json()

    email = get_jwt_identity().get('email')

    user: UserModel = user_query.filter_by(email=email).first()

    try:
        group: GroupModel = group_query.get(group_id)

        if group.owner_id == user.id:
            for key, value in data.items():
                if key == 'title' or key == 'privacy':
                    setattr(group, key, value)
        else:
            return jsonify(error='Permission denied'), HTTPStatus.FORBIDDEN

        session.commit()

        return jsonify(group), HTTPStatus.OK

    except DataError:
        return jsonify(error='Group not found'), HTTPStatus.NOT_FOUND

    except IntegrityError as err:
        if '(psycopg2.errors.UniqueViolation)' in str(err):
            return (
                jsonify(error=f'Group "{group.title}" already exists'),
                HTTPStatus.CONFLICT,
            )
