from flask import Blueprint
from app.controllers.admin_controller import create_admin, login_admin, update_avatar

bp_admin = Blueprint("bp_admin", __name__, url_prefix="/admin")

bp_admin.post("/signup")(create_admin)
bp_admin.post("/login")(login_admin)
bp_admin.patch("/update/<int:id>")(update_avatar)
