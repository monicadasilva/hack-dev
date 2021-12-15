from flask import Blueprint


from app.controllers.event_controller import details_event, pdf_event, read_events, users_event

bp_event = Blueprint("bp_event", __name__, url_prefix="/events")



bp_event.get("/<int:id>")(details_event)
bp_event.get("/pdf/<int:id>")(pdf_event)
bp_event.get("/users/<int:id>")(users_event)
bp_event.get("")(read_events)
