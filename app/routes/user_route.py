from flask import Blueprint

from app.controllers.user_get_controller import main_get

bp = Blueprint("bp_user", __name__, url_prefix="/api/user")

# bp.post("")()
bp.get("")(main_get)
# bp.patch("")()
# bp.delete("")()
