from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref


@dataclass
class EventsModel(db.Model):
    id: int
    name: str
    date: str
    duration: str
    skills_id: int
    sponsors_id: int
    pending: bool

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)
    duration = Column(DateTime, nullable=False)
    description = Column(String, nullable=False)
    skills_id = Column(
        Integer,
        ForeignKey("skills.id"),
        nullable=False
    )
    sponsors_id = Column(
        Integer,
        ForeignKey("sponsors.id"),
        nullable=False
    )
    pending = Column(Boolean, nullable=False)
    skill = db.relationship("SkillsModel", backref=backref("event"), uselist=False)
    sponsor = db.relationship('SponsorModel', backref=backref('event'), uselist=False)