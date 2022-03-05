from flask import Blueprint

from app.controllers.image_post_controller import post_image


bp = Blueprint("bp_image", __name__, url_prefix="/api/image")

bp.post("")(post_image)
