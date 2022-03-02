from flask import Flask

from app.routes.teste import bp
from app.routes.user_route import bp as bp_user

def init_app(app: Flask):
    app.register_blueprint(bp)
    app.register_blueprint(bp_user)