from email.policy import HTTP

from flask import current_app, jsonify, request
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import Query, Session

from app.models.comment_model import CommentModel
from app.models.user_model import UserModel

@jwt_required()
def create_comment(group_id):
    session: Session = current_app.db.session
    user_query: Query = UserModel.query
    comment_query: Query = CommentModel.query
    
    data: dict = request.get_json()
    comment = data["comment"]

    email = get_jwt_identity().get("email")
    user: UserModel = user_query.filter_by(email=email).first()

    new_comment = CommentModel(comment=comment)
    new_comment.user_id = user.id
    new_comment.group_id = group_id

    session.add(new_comment)
    session.commit()

    return jsonify(new_comment),HTTPStatus.CREATED