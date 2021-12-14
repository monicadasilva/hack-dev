from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    from app.models.prize_model import PrizeModel
    from app.models.skills_model import SkillsModel
    from app.models.address_model import AddressModel
    from app.models.group_model import GroupModel
    from app.models.feedback_model import FeedbackModel
    from app.models.users_model import UserModel
    from app.models.sponsors_model import SponsorModel
    from app.models.event_model import EventsModel
    from app.models.admin_model import AdminModel
    from app.models.avatar_model import AvatarModel
    from app.models.company_model import CompanyModel
    from app.models.user_group_table import user_group

    app.db = db
