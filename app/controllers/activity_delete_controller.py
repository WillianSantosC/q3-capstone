from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session

from app.models.activity_model import ActivityModel


@jwt_required()
def activity_delete(id):
    try:
        session: Session = current_app.db.session
        activity: ActivityModel = ActivityModel.query.filter_by(id=id).first()
        session.delete(activity)
        session.commit()
        return '', HTTPStatus.OK
    except:
        return {'msg': 'activity not found'}, HTTPStatus.NOT_FOUND
