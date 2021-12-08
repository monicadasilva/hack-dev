from flask import Flask
from app.routes.user_blueprint import bp as bp_user
from app.routes.admin_blueprint import bp_admin


def init_app(app: Flask):
    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_user)
