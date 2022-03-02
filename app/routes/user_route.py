from flask import Blueprint

from app.controllers.user_get_controller import user_get

bp = Blueprint("bp_user", __name__, url_prefix="/api/user")

# bp.post("")()
bp.get("")(user_get)
# bp.patch("")()
# bp.delete("")()
