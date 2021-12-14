from flask import Blueprint
from app.controllers.user_controller import create_address, create_user, delete_user, login, signup_event, unsub_event, update_avatar, user_avatar, user_info, update_address, update_user, view_prizes
from flask_jwt_extended import jwt_required


bp = Blueprint("bp_user", __name__, url_prefix="/users")

bp.post("/login")(login)

bp.post("/signup")(create_user)
bp.patch("/update/avatar/<int:id>")(update_avatar)
bp.get("/<int:id>")(user_info)
bp.delete("/<int:id>")(delete_user)
bp.post("/address/<int:id>")(create_address)
bp.patch("/address/update/<int:id>")(update_address)
bp.patch("/<int:id>")(update_user)
bp.patch("/event/signup/<int:id>")(signup_event)
bp.get("/prizes")(view_prizes)
bp.get("/avatar/<int:id>")(user_avatar)
bp.patch("/event/unsubscribe/<int:id>")(unsub_event)

