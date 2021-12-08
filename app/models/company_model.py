from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass


@dataclass
class CompanyModel(db.Model):
    id: int
    name: str
    email: str
    avatar_id: int
    mkt_material: str

    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=True)
    avatar_id = Column(Integer, ForeignKey("avatars.id"))
    mkt_material = Column(LargeBinary)

    avatar = relationship("AvatarModel", backref="company", uselist=False)

    @property
    def password(self):
        raise AttributeError("Password not found!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
