from flask import Blueprint
from app.controllers.user_controller import create_user, login, update_avatar

bp = Blueprint("bp_user", __name__, url_prefix="/users")

bp.post("/login")(login)

bp.post("/signup")(create_user)
bp.patch("/update/<int:id>")(update_avatar)
