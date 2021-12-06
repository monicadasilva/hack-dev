from flask import Flask
from app.configs import configs, database, migrations
from app import routes

def create_app():

    app = Flask(__name__)

    configs.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)

    return app