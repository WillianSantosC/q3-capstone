from flask import Blueprint

from flask import Blueprint
from app.controllers.activity_post_controller import activity_post, activity_post_time


bp = Blueprint("bp_activity", __name__, url_prefix="/api/activity")

bp.post("")(activity_post)
bp.post("/time/<id>")(activity_post_time)
