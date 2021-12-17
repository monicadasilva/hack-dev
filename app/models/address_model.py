from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class AddressModel(db.Model):
    id: int
    street: str
    number: int
    district: str
    city: str
    state: str
    zip_code: str

    __tablename__ = "user_address"

    id = Column(Integer, primary_key=True)
    street = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    district = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
