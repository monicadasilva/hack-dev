from flask import Blueprint
from app.controllers.home_controller import home

bp_home = Blueprint("bp_home", __name__)

bp_home.get("/")(home)
