from http import HTTPStatus
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user_model import UserModel

@jwt_required()
def update_user():
    data = request.get_json()
    session = current_app.db.session
    user: UserModel = get_jwt_identity()

    for key, value in data.items():
        if key == 'email':
            UserModel.validate_email(value)
            setattr(user, key, value)
        if key == 'password':
            hashed = UserModel.password(value)
            setattr(user, key, hashed)
        else:
            setattr(user, key, value)

    session.add(user)
    session.commit()

    return jsonify(user), HTTPStatus.OK