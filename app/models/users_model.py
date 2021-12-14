from sqlalchemy.sql.elements import Null
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
    avatar_id: int
    address_id: int
    event_id: int

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=True)
    points = Column(Integer, nullable=False, default=0)
    avatar_id = Column(Integer, ForeignKey("avatars.id"))
    address_id = Column(Integer, ForeignKey("user_address.id"))
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)

    avatar = db.relationship('AvatarModel', backref=backref('users'), uselist=False)

    events = relationship("EventsModel", backref=backref("users"), uselist=False)

    address = db.relationship('AddressModel', backref=backref('users'), uselist=False)

    @property
    def password(self):
        raise AttributeError("Password not found!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
