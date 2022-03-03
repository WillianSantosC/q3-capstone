from flask import Flask

from app.routes.activity_route import bp as bp_activity
from app.routes.teste import bp
from app.routes.user_route import bp as bp_user


def init_app(app: Flask):
    app.register_blueprint(bp)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_activity)
