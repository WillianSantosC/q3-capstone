from flask import Flask

# from app.routes.teste import bp
from app.routes.user_route import bp

def init_app(app: Flask):
    app.register_blueprint(bp)
