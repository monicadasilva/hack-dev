from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class AddressModel(db.Model):
    id: int
    street: str
    number: int
    hood: str
    city: str
    state: str
    zip_code: str

    __tablename__ = "user_address"

    id = Column(Integer, primary_key=True)
    street = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    hood = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    
    # user = db.relationship('UserModel', backref('adress'), uselist=False)