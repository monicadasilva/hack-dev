from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    from app.models.prize_model import PrizeModel
    from app.models.skills_model import SkillsModel
    app.db = db
