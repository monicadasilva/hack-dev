from flask import Flask
from app.configs import configs, cors, database, google, migrations, jwt
from app import routes


def create_app():

    app = Flask(__name__)

    configs.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    jwt.init_app(app)
    google.init_app(app)
    cors.init_app(app)
    routes.init_app(app)
    return app
