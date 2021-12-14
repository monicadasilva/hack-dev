from flask import Flask
from app.configs import configs, cors, database, migrations, jwt
from app import routes
from flask_mail import Mail
mail = Mail()


def create_app():

    app = Flask(__name__)

    configs.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    routes.init_app(app)
    return app
