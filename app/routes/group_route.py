from flask import Blueprint

from app.controllers.group_delete_controller import delete_group
from app.controllers.group_get_controller import group_get
from app.controllers.group_patch_controller import update_group
from app.controllers.group_post_controller import create_group

bp = Blueprint('bp', __name__, url_prefix='/api/group')

bp.get('')(group_get)
bp.post('')(create_group)
bp.patch('/<group_id>')(update_group)
bp.delete('/<group_id>')(delete_group)
