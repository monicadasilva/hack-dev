from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey

@dataclass
class GroupModel(db.Model):


    __tablename__ = 'group'

    id: int
    #event_id: str
    #participants_id: str
    name: str
    mentor_name: str

    id = Column(Integer, primary_key=True)
    #event_id = Column(Integer, ForeignKey('event.id') ,nullable=False )
    #participants_id = Column(Integer, ForeignKey('users.id') ,nullable=False)
    name = Column(String(100))
    mentor_name = Column(String(100))

