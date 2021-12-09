from flask import jsonify
from werkzeug.exceptions import NotFound
from app.models.event_model import EventsModel
from flask_jwt_extended import jwt_required


@jwt_required()
def details_event(id):
    try:
        event = EventsModel.query.filter_by(id=id).first_or_404()
        return jsonify(event)

    except NotFound:
        return {"error": "Event not found"}, 404


@jwt_required()
def read_events():
    events = EventsModel.query.all()

    return jsonify([{
        "id": event.id,
        "name": event.name,
        "description": event.description,
        "date": event.date,
        "pending": event.pending,
        "duration": event.duration,
        "skills": event.skills,
    } for event in events]), 200
