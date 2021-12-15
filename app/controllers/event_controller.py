from flask import jsonify, send_file
from werkzeug.exceptions import NotFound
from app.models.event_model import EventsModel
from flask_jwt_extended import jwt_required
from app.models.users_model import UserModel
from app.utils import generate_event_pdf

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


@jwt_required()
def pdf_event(id):
    try:
        event_one = EventsModel.query.filter_by(id=id).first_or_404()
        users = UserModel.query.filter_by(event_id=event_one.id).all()
        
        generate_event_pdf(event_one.name, users, event_one.date, event_one.duration)

        name = event_one.name.split(' ')[0]
        
        return send_file(f'/tmp/{name}.pdf')
        

    except NotFound:
        return {"error": "Event not found"}, 404



@jwt_required()
def users_event(id):
    try:
        event_one = EventsModel.query.filter_by(id=id).first_or_404()
        users = UserModel.query.filter_by(event_id=event_one.id).all()
        return jsonify({"users": users, "quantity_users": len(users)})

    except NotFound:
        return {"error": "Event not found"}, 404
