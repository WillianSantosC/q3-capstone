from flask import Flask

from app.routes.teste import bp


def init_app(app: Flask):
    app.register_blueprint(bp)
