from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass


@dataclass
class AdminModel(db.Model):
    id: int
    name: str
    email: str


    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=True)
    avatar_id = Column(Integer, ForeignKey("avatars.id"))

    avatar = db.relationship('AvatarModel', backref=backref('admin'), uselist=False)


   

    @property
    def password(self):
        raise AttributeError("Password not found!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
