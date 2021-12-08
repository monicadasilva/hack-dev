from flask import jsonify
from werkzeug.exceptions import NotFound
from app.models.event_model import EventsModel


def details_event(id):
    try:
        event = EventsModel.query.filter_by(id=id).first_or_404()
        return jsonify(event)

    except NotFound:
        return {"error": "Event not found"}, 404