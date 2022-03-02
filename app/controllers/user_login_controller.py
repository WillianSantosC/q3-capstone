from datetime import timedelta
from http import HTTPStatus
from flask import jsonify, request
from app.models.user_model import UserModel
from app.configs.database import db
from flask_jwt_extended import create_access_token


def login():
    data = request.get_json()
    user = UserModel.query.filter_by(email=data['email']).first()

    if not user:
        return {"error": "email not found"}, HTTPStatus.UNAUTHORIZED
    if not user.check_password(data['password']):
        return {"error": "email and password missmatch"},  HTTPStatus.UNAUTHORIZED

    token = create_access_token(user, expires_delta=timedelta(minutes=2))

    return {"access_token": token}, HTTPStatus.OK