from flask import Blueprint


from app.controllers.user_post_controller import post_user
from app.controllers.user_login_controller import login
from app.controllers.user_patch_controller import update_user

bp = Blueprint("bp_user", __name__, url_prefix="/api/user")
bp.post("/register")(post_user)
bp.post("/login")(login)
bp.patch('')(update_user)

