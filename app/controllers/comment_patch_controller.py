from http import HTTPStatus
from sqlite3 import DataError, IntegrityError

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Query, Session

from app.models.comment_model import CommentModel
from app.models.user_model import UserModel


@jwt_required()
def update_comment(group_id, comment_id):
    session: Session = current_app.db.session
    user_query: Query = UserModel.query
    comment_query: Query = CommentModel.query
    data: dict = request.get_json()

    email = get_jwt_identity().get('email')

    user: UserModel = user_query.filter_by(email=email).first()

    try:
        comment: CommentModel = comment_query.get(comment_id)

        if comment.user_id == user.id:
            for key, value in data.items():
                if key == 'comment':
                    setattr(comment, key, (value).capitalize())
        else:
            return jsonify(error='Permission denied'), HTTPStatus.FORBIDDEN

        session.commit()

        return jsonify(comment), HTTPStatus.OK
    except DataError:
        return jsonify(error='Comment not found'), HTTPStatus.NOT_FOUND
