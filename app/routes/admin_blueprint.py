from flask import Blueprint
from app.controllers.admin_controller import admin_avatar, create_admin, create_prize, get_all_admin, get_one_admin, login_admin, update_avatar, update_event


bp_admin = Blueprint("bp_admin", __name__, url_prefix="/admin")



bp_admin.post("/signup")(create_admin)
bp_admin.post("/login")(login_admin)
bp_admin.patch("/update/avatar/<int:id>")(update_avatar)
bp_admin.post("/prizes")(create_prize)
bp_admin.patch("/update/event/<int:id>")(update_event)
bp_admin.get("/avatar/<int:id>")(admin_avatar)
bp_admin.get("/<int:id>")(get_one_admin)
bp_admin.get("")(get_all_admin)
