from sqlalchemy import Column, Integer, String
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class PrizeModel(db.Model):
    id: int
    name: str
    price: str
    amount: str

    __tablename__ = "prizes"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)