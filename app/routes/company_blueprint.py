from flask import Blueprint
from app.controllers.company_controller import create_company, create_event, login_company

bp_company = Blueprint("bp_company", __name__, url_prefix="/company")

bp_company.post("/signup")(create_company)
bp_company.post("/login")(login_company)
bp_company.post("/events")(create_event)
