from flask import Blueprint

from app.controllers.event_controller import details_event

bp_event = Blueprint("bp_event", __name__, url_prefix="/events")

bp_event.get("/<int:id>")(details_event)