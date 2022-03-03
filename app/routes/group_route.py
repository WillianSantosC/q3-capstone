from flask import Blueprint

from app.controllers.group_post_controller import create_group
from app.controllers.group_get_controller import group_get

bp = Blueprint('bp', __name__, url_prefix='/api/group')

bp.post('')(create_group)
bp.get('')(group_get)