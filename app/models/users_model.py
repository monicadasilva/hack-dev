from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass


@dataclass
class UserModel(db.Model):
    id: int
    name: str
    email: str
    points: int
    address_id: int
    event_id: int

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=True)
    points = Column(Integer, nullable=False, default=0)
    avatar = Column(String, nullable=False)
    address_id = Column(Integer, ForeignKey("user_address.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    # token = Column(String, nullable=True)

    events = relationship("EventsModel", backref=backref("users"), uselist=False)

    address = db.relationship('AddressModel', backref=backref('users'), uselist=False)
    
    @property
    def password(self):
        raise AttributeError("Password not found!")

    @password.setter
    def password_to_hash(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

