from flask import Blueprint

from app.controllers.image_controller import (delete_image, get_image,
                                              post_image)

bp = Blueprint('bp_image', __name__, url_prefix='/api/image')

bp.post('')(post_image)
bp.patch('')(post_image)
bp.get('/<id>')(get_image)
bp.delete('/<id>')(delete_image)
