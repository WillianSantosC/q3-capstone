from flask import Blueprint

from app.controllers.group_post_controller import create_group

bp = Blueprint('bp', __name__, url_prefix='/api/group')

bp.post('')(create_group)
