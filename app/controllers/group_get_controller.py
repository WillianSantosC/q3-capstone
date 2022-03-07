from http import HTTPStatus

import sqlalchemy
from flask import current_app, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session

from app.models.group_model import GroupModel


@jwt_required()
def group_get():

    try:
        groups = GroupModel.query.all()
        return jsonify(groups), HTTPStatus.OK

    except sqlalchemy.exc.ProgrammingError:
        return (
            jsonify({'message': 'Ainda não existem grupos cadastrados'}),
            HTTPStatus.OK,
        )
