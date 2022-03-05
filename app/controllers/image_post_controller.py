from http import HTTPStatus
from tkinter import Image
from flask import current_app, request

from app.models.image_model import ImageModel
from sqlalchemy.orm import Session
from flask_jwt_extended import get_jwt_identity, jwt_required

import base64

from app.models.user_model import UserModel


@jwt_required()
def post_image():
    email = get_jwt_identity().get("email")
    user: UserModel = UserModel.query.filter_by(email=email).first()

    session: Session = current_app.db.session

    file = request.files["image"]
    new_image = base64.b64encode(file.read())
    image = ImageModel()
    image.image = new_image
    image.user_id = user.id
    session.add(image)
    session.commit()
    return "", HTTPStatus.OK
