from flask import Blueprint

from app.controllers.comment_post_controller import create_comment
from app.controllers.comment_get_controller import comment_get

bp = Blueprint('bp_comment', __name__, url_prefix='/api/<group_id>/comment')

bp.post('')(create_comment)
bp.get('')(comment_get)
