from flask import Blueprint
from app.controllers.admin_controller import create_admin

bp_admin = Blueprint("bp_admin", __name__, url_prefix="/admin")

bp_admin.post("/signup")(create_admin)