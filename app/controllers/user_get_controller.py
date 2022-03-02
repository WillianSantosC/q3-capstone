from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def user_get():
    user = get_jwt_identity()
    return jsonify(user), HTTPStatus.OK
