from http import HTTPStatus
from sqlite3 import DataError

from flask import current_app, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import DataError
from sqlalchemy.orm import Query, Session

from app.models.comment_model import CommentModel
from app.models.user_model import UserModel


@jwt_required()
def delete_comment(group_id, comment_id):
    session: Session = current_app.db.session
    user_query: Query = UserModel.query
    comment_query: Query = CommentModel.query

    email = get_jwt_identity().get('email')

    user: UserModel = user_query.filter_by(email=email).first()

    try:
        comment: CommentModel = comment_query.get(comment_id)

        if comment.user_id == user.id:
            session.delete(comment)
            session.commit()
            return '', HTTPStatus.NO_CONTENT
        else:
            return jsonify(error='Permission denied'), HTTPStatus.FORBIDDEN

    except DataError:
        return jsonify(error='comment not found'), HTTPStatus.NOT_FOUND
