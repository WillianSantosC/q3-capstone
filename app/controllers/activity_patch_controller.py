from http import HTTPStatus
from flask import current_app, request
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session

from app.models.activity_model import ActivityModel


@jwt_required()
def activity_patch(id):
    session: Session = current_app.db.session
    data = request.get_json()
    try:
        activity: ActivityModel = ActivityModel().query.filter_by(id=id).first()
        activity.favorite = data["favorite"]
        session.add(activity)
        session.commit()
        return "", HTTPStatus.OK
    except:
        return {"msg": "activity not found"}, HTTPStatus.OK
