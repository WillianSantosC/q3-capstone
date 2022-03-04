from flask import Flask

from app.routes.activity_route import bp as bp_activity
from app.routes.comment_route import bp as bp_comment
from app.routes.group_route import bp as bp_group
from app.routes.user_route import bp as bp_user


def init_app(app: Flask):
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_activity)
    app.register_blueprint(bp_group)
    app.register_blueprint(bp_comment)
