from flask import Flask
from app.routes.user_blueprint import bp as bp_user
from app.routes.admin_blueprint import bp_admin
from app.routes.event_blueprint import bp_event
from app.routes.company_blueprint import bp_company
from app.routes.home_blueprint import bp_home


def init_app(app: Flask):
    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_event)
    app.register_blueprint(bp_company)
    app.register_blueprint(bp_home)
