from flask import Blueprint

from app.controllers.card_patch_controller import update_card


bp = Blueprint('bp_card', __name__, url_prefix='/api/card')
bp.patch('/<id>')(update_card)