from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey

user_group = db.Table(
    "event_group",
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("group_id", Integer, ForeignKey("group.id"))
)
