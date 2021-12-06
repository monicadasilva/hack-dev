from sqlalchemy import Column, Integer, String
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class SkillsModel(db.Model):
    id: int
    name: str

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)