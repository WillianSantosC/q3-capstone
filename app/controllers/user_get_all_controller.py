from http import HTTPStatus

from flask import jsonify

from app.models.user_model import UserModel
from app.services.sum_time import sum_time


def user_get_all():
    users: UserModel = UserModel().query.all()
    new_users = []
    timer_general = '00:00:00'

    for user in users:
        for time in user.activity:
            timer_general = sum_time(timer_general, time.timer_total)

        new_users.append(
            {'name': user.name, 'timer_general': str(timer_general)}
        )

    return jsonify(
        sorted(new_users, key=lambda x: x['timer_general'], reverse=True)
    )
