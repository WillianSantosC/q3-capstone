from flask import Blueprint

from app.controllers.activity_post_controller import (activity_post,
                                                      activity_post_pause,
                                                      activity_post_play)

bp = Blueprint('bp_activity', __name__, url_prefix='/api/activity')

bp.post('')(activity_post)
bp.post('/play/<id>')(activity_post_play)
bp.post('/pause/<id>')(activity_post_pause)
