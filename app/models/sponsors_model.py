from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship
from dataclasses import dataclass


@dataclass
class SponsorModel(db.Model):
    id: int
    name: str

    __tablename__ = "sponsors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
