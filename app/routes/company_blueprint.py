from flask import Blueprint
from app.controllers.company_controller import authorize, create_company, create_event, get_all_companies, get_one_company, google_login, login_company, logout, recuperate_password


bp_company = Blueprint("bp_company", __name__, url_prefix="/company")



bp_company.post("/signup")(create_company)
bp_company.post("/login")(login_company)
bp_company.post("/events")(create_event)
bp_company.get("/<int:id>")(get_one_company)
bp_company.get("")(get_all_companies)
bp_company.patch("/recuperate/password")(recuperate_password)
bp_company.get("/login/google")(google_login)
bp_company.get("/authorize")(authorize)
bp_company.get("/logout")(logout)
