from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
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

    try:
        new_group: GroupModel = GroupModel(title=data.get('title'))

        new_group.owner_id = user.id

        user.groups.append(new_group)

        session.add(new_group)
        session.commit()

        return jsonify(new_group), HTTPStatus.CREATED

    except IntegrityError as err:
        if '(psycopg2.errors.UniqueViolation)' in str(err):
            return (
                jsonify(error=f'Group "{new_group.title}" already exists'),
                HTTPStatus.CONFLICT,
            )
