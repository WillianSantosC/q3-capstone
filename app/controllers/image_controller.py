from http import HTTPStatus

from flask import Response, current_app, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Session

from app.models.image_model import ImageModel
from app.models.user_model import UserModel


@jwt_required()
def post_image():
    session: Session = current_app.db.session

    email = get_jwt_identity().get('email')

    user: UserModel = UserModel.query.filter_by(email=email).first()

    user_image: ImageModel = ImageModel.query.filter_by(
        user_id=user.id
    ).first()

    file = request.files['image']
    mimetype = file.mimetype

    if user_image:
        session.delete(user_image)
        session.commit()

    if not file:
        return {'msg': 'no image uploaded!'}, HTTPStatus.BAD_REQUEST

    if not mimetype.split('/')[1] in ['png', 'jpg', 'jpeg']:
        return {'msg': 'incorrect format'}, HTTPStatus.BAD_REQUEST

    # if len(file.read()) / 1024 < 15:
    #     return {'msg': 'image size too large'}, HTTPStatus.BAD_REQUEST

    image = ImageModel(
        name=file.name, image=file.read(), mimetype=mimetype, user_id=user.id
    )

    session.add(image)
    session.commit()

    return {'id': image.id}, HTTPStatus.OK


def get_image(id):
    image = ImageModel.query.filter_by(id=id).first()

    if not image:
        return {'msg': 'not found'}, HTTPStatus.NOT_FOUND

    return Response(image.image, mimetype=image.mimetype), HTTPStatus.OK


@jwt_required()
def delete_image(id):
    session: Session = current_app.db.session

    image: ImageModel = ImageModel.query.filter_by(id=id).first()

    session.delete(image)
    session.commit()

    return '', HTTPStatus.OK
