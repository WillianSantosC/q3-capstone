from datetime import timedelta
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import create_access_token

from app.configs.database import db
from app.models.user_model import UserModel


def login():
    data = request.get_json()
    user = UserModel.query.filter_by(email=data['email']).first()

    if not user:
        return {'error': 'email not found'}, HTTPStatus.UNAUTHORIZED
    if not user.check_password(data['password']):
        return {
            'error': 'email and password missmatch'
        }, HTTPStatus.UNAUTHORIZED

    token = create_access_token(user)

    return {'access_token': token}, HTTPStatus.OK
