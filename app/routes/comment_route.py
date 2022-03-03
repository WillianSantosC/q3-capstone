from flask import Blueprint

from app.controllers.comment_post_controller import create_comment

bp = Blueprint('bp_comment', __name__, url_prefix='/api/<group_id>/comment')

bp.post('')(create_comment)
