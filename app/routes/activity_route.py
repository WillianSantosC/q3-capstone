from flask import Blueprint
from app.controllers.activity_delete_controller import activity_delete
from app.controllers.activity_get_controller import activity_get
from app.controllers.activity_patch_controller import activity_patch

from app.controllers.activity_post_controller import (
    activity_post,
    activity_post_pause,
    activity_post_play,
)

bp = Blueprint("bp_activity", __name__, url_prefix="/api/activity")

bp.post("")(activity_post)
bp.post("/play/<id>")(activity_post_play)
bp.post("/pause/<id>")(activity_post_pause)
bp.get("/<id>")(activity_get)
bp.patch("/<id>")(activity_patch)
bp.delete("/<id>")(activity_delete)
