from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask import Flask, jsonify, request
from app.configs.database import db
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

        result = {
            "name": user.name,
            "email": user.email
        }

        return result, HTTPStatus.CREATED


    except IntegrityError as err:
        if "psycopg2.errors.UniqueViolation" in  str(err):
            return {"error": "email already exists"}, HTTPStatus.CONFLICT
    
    except EmailError as error:
        return error.message, error.code

