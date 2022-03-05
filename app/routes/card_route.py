from flask import Blueprint
from app.controllers.card_get_controller import get_card

from app.controllers.card_patch_controller import update_card
from app.controllers.card_post_controller import create_card


bp = Blueprint('bp_card', __name__, url_prefix='/api/card')
bp.post('/<activity_id>')(create_card)
bp.get('<id>')(get_card)
bp.patch('/<id>')(update_card)