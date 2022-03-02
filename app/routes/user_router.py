from flask import Blueprint
from app.controllers.user_delete_controller import user_delete

bp = Blueprint("bp_user", __name__, url_prefix="/api/user")

# bp.post("")()
# bp.get("")()
# bp.patch("")()
bp.delete("")(user_delete)
