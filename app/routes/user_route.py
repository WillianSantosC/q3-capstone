from flask import Blueprint
from app.controllers.user_patch_controller import update_user

bp = Blueprint("bp_user_patch", __name__, url_prefix="/api/user")

bp.patch('')(update_user)