from sqlalchemy.sql.sqltypes import LargeBinary
from app.configs.database import db
from sqlalchemy import Column, Integer, Text
from dataclasses import dataclass

@dataclass
class AvatarModel(db.Model):
    id: int
    data: str
    name: str



    __tablename__ = "avatars"

    id = Column(Integer, primary_key=True)
    data = Column(LargeBinary)
    name = Column(Text, nullable=False)