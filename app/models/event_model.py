from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, ARRAY
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref


@dataclass
class EventsModel(db.Model):
    id: int
    name: str
    description: str
    date: str
    duration: str
    skills: str
    sponsors_id: int
    pending: bool

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)
    duration = Column(DateTime, nullable=False)
    description = Column(String, nullable=False)
    skills = Column(String, nullable=False)
    sponsors_id = Column(
        Integer,
        ForeignKey("company.id")
    )
    pending = Column(Boolean, default=False)
    sponsor = db.relationship('CompanyModel', backref=backref('event'), uselist=False)
