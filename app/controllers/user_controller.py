from flask import request, current_app, jsonify
from sqlalchemy.util.langhelpers import NoneType
from werkzeug.utils import secure_filename
from app.controllers import verify
from app.exceptions.exceptions import AddressError, InvalidInput, InvalidKey
from app.models.address_model import AddressModel
from app.models.avatar_model import AvatarModel
from app.models.event_model import EventsModel
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token
from sqlalchemy import exc
from werkzeug.exceptions import NotFound
from flask_jwt_extended import jwt_required


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

        return {'id': user.id, 'name': user.name, 'email': user.email, 'password': user.password_hash, 'points': user.points}, 201

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

        session.commit()

        if user.address == None:
            raise AddressError

        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": {
                "street": user.address.street,
                "number": user.address.number,
                "district": user.address.district,
                "city": user.address.city,
                "state": user.address.state,
                "zip_code": user.address.zip_code
            }
        }), 200
        
    except NotFound:
        return {"error": "User not found"}, 404
    except AddressError:
         return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        }), 200

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
def update_address(id):
    session = current_app.db.session
    data = request.get_json()
    
    address = AddressModel(**data)
    session.add(address)
    session.commit()
    
    user = UserModel.query.filter_by(id=id).update({'address_id': address.id})
    session.commit()
    
    return {'msg': 'Address registered!'}

@jwt_required()
def update_user(id):

    try:
        session = current_app.db.session
        data = request.get_json()
        
        user = UserModel.query.get(id)
        
        if not user:
            raise NotFound()

        for key, value in data.items():
            setattr(user, key, value)

        session.add(user)
        session.commit()

        return jsonify(user)

    except NotFound:
        return {"error": "User not found"}, 404


@jwt_required()
def signup_event(id):
    session = current_app.db.session
    data = request.get_json()
    name = data['name']
    
    try:
        event = EventsModel.query.filter_by(name=name).one()
        
        if event == None:
            raise NotFound()
        
        user = UserModel.query.filter_by(id=id).update({'event_id': event.id})
        
        
        event = EventsModel.query.get(id)
        
        session.commit()
        
        return {'id': event.id, 'name': event.name, 'date': event.date, 'duration': event.duration, 'description': event.description }, 200       
    
    except NotFound:
        return {"error": "Event not found"}, 404