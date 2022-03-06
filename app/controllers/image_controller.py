from http import HTTPStatus
from http.client import UNSUPPORTED_MEDIA_TYPE
from xmlrpc.client import UNSUPPORTED_ENCODING
from flask import Response, current_app, request

from app.models.image_model import ImageModel
from sqlalchemy.orm import Session
from flask_jwt_extended import get_jwt_identity, jwt_required


from app.models.user_model import UserModel


@jwt_required()
def post_image():
    email = get_jwt_identity().get("email")

    user: UserModel = UserModel.query.filter_by(email=email).first()

    session: Session = current_app.db.session

    img: ImageModel = ImageModel.query.filter_by(user_id=user.id).first()

    if img:
        session.delete(img)
        session.commit()

    file = request.files["image"]
    mimetype = file.mimetype

    image = ImageModel(
        name=file.name, image=file.read(), mimetype=mimetype, user_id=user.id
    )

    session.add(image)
    session.commit()
    return {"id": image.id}, HTTPStatus.OK


def get_image(id):
    image = ImageModel.query.filter_by(id=id).first()
    if not image:
        return {"msg": "not found"}, HTTPStatus.NOT_FOUND
    return Response(image.image, mimetype=image.mimetype), HTTPStatus.OK


@jwt_required()
def delete_image(id):
    session: Session = current_app.db.session

    img: ImageModel = ImageModel.query.filter_by(id=id).first()

    session.delete(img)
    session.commit()
    return "", HTTPStatus.OK
