from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError

from app.models.user_model import UserModel


@jwt_required()
def update_user():
    data = request.get_json()
    session = current_app.db.session
    user_identity = get_jwt_identity()
    user: UserModel = UserModel.query.filter_by(
        email=user_identity['email']
    ).first()

    try:
        for key, value in data.items():
            if key == 'email':
                user.validate_email(key, value)
                setattr(user, key, value)
            if key == 'name':
                setattr(user, key, value.title())
            if key == 'password':
                password_to_hash = data['password']
                user.password = password_to_hash

        session.add(user)
        session.commit()

        return '', HTTPStatus.OK

    except IntegrityError as err:
        if '(psycopg2.errors.UniqueViolation)' in str(err):
            return (
                jsonify(error=f'email already exists'),
                HTTPStatus.CONFLICT,
            )
