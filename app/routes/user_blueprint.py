from flask import Blueprint
from app.controllers.user_controller import create_user, delete_user, login, update_avatar, user_info

bp = Blueprint("bp_user", __name__, url_prefix="/users")

bp.post("/login")(login)

bp.post("/signup")(create_user)
bp.patch("/update/<int:id>")(update_avatar)
bp.get("/<int:id>")(user_info)
bp.delete("/<int:id>")(delete_user)