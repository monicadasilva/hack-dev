from sqlalchemy.sql.sqltypes import Integer
from app.configs.database import db
from sqlalchemy import Column, Text ,ForeignKey
from dataclasses import dataclass

@dataclass
class FeedbackModel(db.Model):


    id: int
    event_id: int
    user_id: int
    feedback: str

    __tablename__ = 'feedbacks'
    
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    feedback = Column(Text)