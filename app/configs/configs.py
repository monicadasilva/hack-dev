import os
from flask import Flask
from dotenv import load_dotenv
from datetime import timedelta



load_dotenv()


def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=15)
    app.secret_key = os.getenv("SECRET_KEY")
    app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
 

