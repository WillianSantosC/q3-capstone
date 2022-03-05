from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user_model import UserModel
from app.services.sum_time import sum_time


@jwt_required()
def user_get():
    email = get_jwt_identity().get('email')
    user: UserModel = UserModel().query.filter_by(email=email).first()
    timer_general = '00:00:00'
    for act in user.activity:
        timer_general = sum_time(timer_general, act.timer_total)

    return jsonify(
        {
            'name': user.name,
            'timer_general': str(timer_general),
            'activity': user.activity,
        }
    )
