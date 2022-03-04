from flask import Blueprint
from app.controllers.comment_delete_controller import delete_comment
from app.controllers.comment_patch_controller import update_comment

from app.controllers.comment_post_controller import create_comment
from app.controllers.comment_get_controller import comment_get

bp = Blueprint('bp_comment', __name__, url_prefix='/api/<group_id>/comment')

bp.post('')(create_comment)
bp.get('')(comment_get)
bp.patch('/<comment_id>')(update_comment)
bp.delete('/<comment_id>')(delete_comment)
