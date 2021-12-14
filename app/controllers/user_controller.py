from flask import request, current_app, jsonify, send_file
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from sqlalchemy.util.langhelpers import NoneType
from werkzeug.utils import secure_filename
from app.controllers import verify
from app.exceptions.exceptions import AddressError, AvatarError, InvalidInput, InvalidKey
from app.models.address_model import AddressModel
from app.models.avatar_model import AvatarModel
from app.models.event_model import EventsModel
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token
from sqlalchemy import exc
from werkzeug.exceptions import NotFound
from flask_jwt_extended import jwt_required
from app.models.prize_model import PrizeModel
from io import BytesIO


def login():
    try:
        data = request.get_json()

        user: UserModel = UserModel.query.filter_by(
            email=data["email"]).first()

        if user.verify_password(data["password"]):
            token = create_access_token(user)
            return jsonify({
                "token": token,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "points": user.points,
                    "address": user.address,
                    "event": user.events
                }
            }), 200
        else:
            return jsonify({"msg": "Incorrect password"}), 400
    except KeyError as e:
        return jsonify({"expected_key": e.args}), 400
    except AttributeError:
        return jsonify({"msg": "incorrect or unregistered email"}), 400


def create_user():
    session = current_app.db.session
    data = request.get_json()

    try:
        verify(data)
        user = UserModel(**data)
        session.add(user)
        session.commit()

        return {'id': user.id, 'name': user.name, 'email': user.email, 'points': user.points}, 201

    except InvalidInput as error:
        return(*error.args, 400)

    except InvalidKey as error:
        return(*error.args, 400)

    except exc.IntegrityError:
        return {'msg': 'This email already registered!'}, 409


@jwt_required()
def update_avatar(id):
    session = current_app.db.session
    user_avatar = request.files['avatar']

    user = UserModel.query.filter_by(id=id).first_or_404()

    if user.avatar_id != None:
        old_avatar = AvatarModel.query.get(user.avatar_id)
        session.delete(old_avatar)
        session.commit()

    filename = secure_filename(user_avatar.filename)
    img = AvatarModel(data=user_avatar.read(), name=filename)
    session.add(img)
    session.commit()

    UserModel.query.filter_by(id=id).update({'avatar_id': img.id})
    session.commit()

    return '', 204


@jwt_required()
def user_info(id):
    try:
        session = current_app.db.session
        user = UserModel.query.filter_by(id=id).first_or_404()
        event = EventsModel.query.filter_by(id=user.event_id).first()

        session.commit()
        
        if event == None:
            return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
        }), 200

        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "event": event
        }), 200

    except NotFound:
        return {"error": "User not found"}, 404


@jwt_required()
def delete_user(id):
    try:
        session = current_app.db.session
        query = UserModel.query.filter_by(id=id).first_or_404()

        session.delete(query)
        session.commit()

        return "ok", 204
    except NotFound:
        return {"error": "User not found"}, 404


@jwt_required()
def create_address(id):

    try:
        session = current_app.db.session
        data = request.get_json()

        user: UserModel = UserModel.query.get(id)
        addrres_local = AddressModel(**data)

        if not user:
            raise NotFound()

        session.add(addrres_local)
        session.commit()

        user.address_id = addrres_local.id

        session.add(user)
        session.commit()

        return jsonify(addrres_local)

    except NotFound:
        return jsonify({"error": "User not found"}), 404

    except exc.IntegrityError:
        return jsonify({"expected_keys": ["street", "number", "district", "city", "state", "zip_code"], "received": [key for key in data.keys()]}), 409


@jwt_required()
def update_address(id):
    session = current_app.db.session
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(id=id).first()
    address = AddressModel.query.filter_by(id=user.address.id).update(data)

    session.commit()

    return {'msg': 'Address registered!'}


@jwt_required()
def update_user(id):

    try:
        session = current_app.db.session
        data = request.get_json()

        user = UserModel.query.get_or_404(id)

        for key, value in data.items():
            setattr(user, key, value)

        session.add(user)
        session.commit()

        return {'name': user.name, 'email': user.email}

    except NotFound:
        return {"error": "User not found"}, 404


@jwt_required()
def signup_event(id):
    session = current_app.db.session
    data = request.get_json()
    name = data['name']

    try:
        event = EventsModel.query.filter_by(name=name).first_or_404()

        UserModel.query.filter_by(id=id).update({'event_id': event.id})

        session.commit()

        return {'id': event.id, 'name': event.name, 'date': event.date, 'duration': event.duration, 'description': event.description}, 200

    except NotFound:
        return {"error": "Event not found"}, 404


@jwt_required()
def view_prizes():

    prize = PrizeModel.query.all()

    return jsonify({"data": prize})


@jwt_required()
def user_avatar(id):
    try:
        avatar = UserModel.query.filter_by(id=id).first_or_404()
        file_data = AvatarModel.query.filter_by(id=avatar.avatar_id).one()

        return send_file(BytesIO(file_data.data), attachment_filename=file_data.name, as_attachment=False)

    except NotFound:
        return {"error": "User not found"}, 404
    except exc.NoResultFound:
        return {"error": "Avatar not found"}, 404


@jwt_required()
def unsub_event(id):
    session = current_app.db.session

    try:
        user = UserModel.query.filter_by(id=id).first_or_404()
        
        if user.event_id:        
            UserModel.query.filter_by(id=id).update({'event_id': None})
            session.commit()
            return {'msg': 'Successfully unsubscribed from event.'}, 200
        
        return {"error": "User not subscribed in any event."}, 404

    except NotFound:
        return {"error": "User not found."}, 404
