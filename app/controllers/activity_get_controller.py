from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.activity_model import ActivityModel


@jwt_required()
def activity_get(id):
    activity: ActivityModel = ActivityModel().query.filter_by(id=id).first()
    if activity != None:
        return jsonify(activity), HTTPStatus.OK
    else:
        return {"msg": "activity not found"}, HTTPStatus.NOT_FOUND
