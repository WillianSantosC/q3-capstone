from flask import Blueprint
# from app.controllers.user_get_controller import main_get
from app.controllers.user_post_controller import post_user


bp = Blueprint("bp_user", __name__, url_prefix="/api/user")
bp.post("")(post_user)
# bp.get("")(main_get)
# bp.patch("")()
# bp.delete("")()