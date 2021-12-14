from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from app.models.user_group_table import user_group


@dataclass
class GroupModel(db.Model):

    __tablename__ = 'group'

    id: int
    event_id: str
    event: dict
    users: list

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)

    event = relationship("EventsModel", backref=backref("group"), uselist=False)
    users = relationship("UserModel", secondary=user_group, backref=backref("group", uselist=False))
