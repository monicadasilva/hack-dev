from flask import Blueprint
from app.controllers.user_controller import login

bp = Blueprint("bp_user", __name__, url_prefix="/users")

bp.post("/login")(login)
