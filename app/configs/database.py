from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.activity_model import ActivityModel
    from app.models.card_model import CardModel
    from app.models.category_model import CategoryModel
    from app.models.comment_model import CommentModel
    from app.models.group_model import GroupModel
    from app.models.image_model import ImageModel
    from app.models.user_model import UserModel
    from app.models.users_groups_table import users_groups
