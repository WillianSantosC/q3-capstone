from app.models.group_model import GroupModel
from http import HTTPStatus

from flask import current_app, jsonify
from sqlalchemy.orm import Session
from flask_jwt_extended import jwt_required

from app.models.user_model import UserModel

@jwt_required()
def group_get():
    session: Session = current_app.db.session
    groups = GroupModel.query.all()
    return jsonify(groups),HTTPStatus.OK