from flask import Blueprint

from app.controllers.image_controller import get_image, post_image, delete_image


bp = Blueprint("bp_image", __name__, url_prefix="/api/image")

bp.post("")(post_image)
bp.get("/<id>")(get_image)
bp.delete("/<id>")(delete_image)
