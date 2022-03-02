from flask import Blueprint
# from app.controllers.user_get_controller import main_get
from app.controllers.user_post_controller import post_user
from app.controllers.user_login_controller import login

bp = Blueprint("bp_user", __name__, url_prefix="/api/user")
bp.post("/register")(post_user)
bp.post("/login")(login) 
# bp.get("")(main_get)
# bp.patch("")()
# bp.delete("")()