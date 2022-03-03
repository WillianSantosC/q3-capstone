from datetime import datetime
from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Session

from app.models.activity_model import ActivityModel
from app.models.category_model import CategoryModel
from app.models.user_model import UserModel
from app.services.sum_time import sum_time


@jwt_required()
def activity_post():
    session: Session = current_app.db.session

    data = request.get_json()
    name = data["name"]

    email = get_jwt_identity().get("email")

    user: UserModel = UserModel.query.filter_by(email=email).first()

    category = CategoryModel.query.filter_by(name=name).first()
    if not category:
        new_category = CategoryModel(name=name)
        session.add(new_category)
        session.commit()

    category = CategoryModel.query.filter_by(name=name).first()

    activity = ActivityModel()
    activity.category_id = category.id
    activity.user_id = user.id

    session.add(activity)
    session.commit()

    return jsonify(activity), HTTPStatus.CREATED


@jwt_required()
def activity_post_time(id):
    session: Session = current_app.db.session
    activity: ActivityModel = ActivityModel().query.filter_by(id=id).first()
    format_year = "%Y-%m-%d %H:%M:%S"
    now = datetime.now().strftime(format_year)
    if activity.timer_init == "null":
        activity.timer_init = now

    else:
        if activity.timer_total != "null":
            more_time = datetime.strptime(now, format_year) - datetime.strptime(
                activity.timer_init, format_year
            )

            activity.timer_total = sum_time(
                activity.timer_total,
                more_time,
            )

            activity.timer_init = "null"

        else:
            new_time = datetime.strptime(now, format_year) - datetime.strptime(
                activity.timer_init, format_year
            )
            activity.timer_total = new_time

    session.add(activity)
    session.commit()

    return jsonify(activity), HTTPStatus.OK
