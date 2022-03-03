from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.models.group_model import GroupModel
from app.models.user_model import UserModel
from app.services.exceptions import EmailError


def post_user():

    try:
        data = request.get_json()
        password_to_hash = data.pop('password')
        user = UserModel(**data)
        user.password = password_to_hash
        db.session.add(user)
        db.session.commit()

        result = {'name': user.name, 'email': user.email}

        return result, HTTPStatus.CREATED

    except IntegrityError as err:
        if 'psycopg2.errors.UniqueViolation' in str(err):
            return {'error': 'email already exists'}, HTTPStatus.CONFLICT

    except EmailError as error:
        return error.message, error.code


@jwt_required()
def add_in_group():
    session: Session = current_app.db.session
    user_query: Query = UserModel.query
    group_query: Query = GroupModel.query
    data: dict = request.get_json()

    email = get_jwt_identity().get('email')

    user: UserModel = user_query.filter_by(email=email).first()

    group: GroupModel = group_query.filter_by(title=data.get('title')).first()

    user.groups.append(group)

    session.commit()

    return (
        jsonify(msg=f'User registered to group `{group.title}`'),
        HTTPStatus.OK, 
    )
