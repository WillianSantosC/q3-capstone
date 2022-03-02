from flask import Blueprint

from app.controllers.teste import testando

bp = Blueprint('bp', __name__, url_prefix='/')

bp.get('')(testando)
