from http import HTTPStatus
from os import getenv

from flask import Flask

from app import routes
from app.configs import database, jwt, migrations


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1000 * 1000

    @app.errorhandler(413)
    def request_entity_too_large(error):
        return {
            'error': 'request entity too large'
        }, HTTPStatus.REQUEST_ENTITY_TOO_LARGE

    database.init_app(app)
    migrations.init_app(app)
    jwt.init_app(app)
    routes.init_app(app)

    return app
