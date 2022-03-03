from http import HTTPStatus
from flask import current_app, request, jsonify
from app.models.category_model import CategoryModel
from app.models.activity_model import ActivityModel
from sqlalchemy.orm import Session
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime
from app.models.user_model import UserModel


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

    if activity.timer_init == "null":
        activity.timer_init = datetime.datetime.now()

    else:
        activity.timer_total = (
            datetime.datetime.strptime(activity.timer_init, "%Y-%m-%d %H:%M:%S.%f")
            - datetime.datetime.now()
        )

        activity.timer_init = "null"

    session.add(activity)
    session.commit()

    return jsonify(activity), HTTPStatus.OK
