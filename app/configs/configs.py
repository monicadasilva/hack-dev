import os
from flask import Flask
from dotenv import load_dotenv


load_dotenv()


def init_app(app:Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))
    app.config["JSON_SORT_KEYS"] = False
