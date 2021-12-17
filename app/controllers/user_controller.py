from flask import request, current_app, jsonify, send_file, redirect, url_for, session
from werkzeug.utils import secure_filename, send_from_directory
from app.controllers import generate_password, token_decoded, verify, verify_owner
from app.exceptions.exceptions import AddressError, AvatarError, InvalidInput, InvalidKey
from app.models.address_model import AddressModel
from app.models.admin_model import AdminModel
from app.models.avatar_model import AvatarModel
from app.models.event_model import EventsModel
from app.models.feedback_model import FeedbackModel
from app.models.group_model import GroupModel
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token
from sqlalchemy import exc
from werkzeug.exceptions import NotFound
from flask_jwt_extended import jwt_required
from app.models.prize_model import PrizeModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import smtplib
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv
from io import BytesIO
from app.configs.google import oauth, google
from app.utils import generate_pdf


load_dotenv()


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
                    "address": user.address
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
        user: UserModel = UserModel.query.filter_by(id=id).first_or_404()
        session.commit()

        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "event": user.events,
            "points": user.points,
            "group": user.group,
            "feedbacks": user.feedback
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
    try:
        user: UserModel = UserModel.query.filter_by(id=id).first_or_404()

        if user.address_id == None:
            address = AddressModel(**data)
            session.add(address)
            session.commit()
            user.address_id = address.id
            session.commit()

        AddressModel.query.filter_by(id=user.address_id).update(data)
        session.commit()

        if not user:
            raise NotFound()

        return {'msg': 'Address registered!'}

    except NotFound:
        return jsonify({"error": "User not found"}), 404


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

        return {'id': event.id, 'name': event.name, 'date': event.date, 'duration': event.duration, 'description': event.description, 'invitation': 'https://discord.gg/ApVraPPX'}, 200

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
def create_group(id):
    try:
        session = current_app.db.session
        data = request.get_json()

        user: UserModel = UserModel.query.filter_by(id=id).first_or_404()
        group = GroupModel(event_id=user.event_id)
        group.users.append(user)

        if bool(data):
            for username in data["users"]:
                _user = UserModel.query.filter_by(name=username).first()
                if not _user.event_id:
                    raise InvalidInput
                group.users.append(_user)

        session.add(group)
        session.commit()

        return jsonify(group), 201
    except exc.IntegrityError:
        return jsonify({"msg": "you need to be registered for an event to create a group"}), 400
    except NotFound:
        return jsonify({"msg": "User not found"}), 404
    except InvalidInput:
        return jsonify({"msg": "one or more users are not registered for an event"}), 400


def recuperate_password():

    try:
        session = current_app.db.session
        data = request.get_json()
        new_password = generate_password(10)

        emailto = data['email']

        UserModel.query.filter_by(email=data['email']).first_or_404()

        UserModel.query.filter_by(email=data['email']).update({'password_hash': generate_password_hash(new_password)})

        session.commit()

        email_send = MIMEMultipart()
        password = os.environ.get(
            'EMAIL_PASS')
        message = f"Sua nova senha: {new_password}"
        email_send["From"] = os.environ.get(
            'EMAIL')
        email_send["To"] = emailto
        email_send["Subject"] = f"Sua nova senha gerada {new_password}"
        email_send.attach(MIMEText(message, "plain"))
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
            server.login(email_send["From"], password)
            server.sendmail(email_send["From"], email_send["To"], email_send.as_string())
        return {"message": "Email sent"}
    except NotFound:
        return {"error": "Email Not Found"}, 404


@jwt_required()
def unsub_event(id):
    session = current_app.db.session

    try:
        user = UserModel.query.filter_by(id=id).first_or_404()

        if user.event_id:
            UserModel.query.filter_by(id=id).update({'event_id': None})
            if user.group:
                group = GroupModel.query.filter_by(id=user.group.id).first()
                if len(group.users) == 0:
                    session.delete(group)
                user.group = None
            session.commit()
            return {'msg': 'Successfully unsubscribed from event.'}, 200

        return {"error": "User not subscribed in any event."}, 404

    except NotFound:
        return {"error": "User not found."}, 404


def google_login():
    google = oauth.create_client('google')
    redirect_uri = url_for('bp_user.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


def authorize():
    dbsession = current_app.db.session

    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    user = oauth.google.userinfo()

    user_data = {'name': user.name, 'email': user.email}
    user_db = UserModel.query.filter_by(email=user.email).first()

    if user_db == None:
        new_user = UserModel(**user_data)
        dbsession.add(new_user)
        dbsession.commit()
        return jsonify({
            "token": token,
            "user": {
                "id": new_user.id,
                "name": new_user.name,
                "email": new_user.email,
                "points": new_user.points,
                "address": new_user.address
            }
        }), 200

    session['profile'] = user_info
    session.permanent = True
    return jsonify({'name': user.name, 'email': user.email, 'avatar': user.picture}), 200


def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


@jwt_required()
def create_feedback(id):
    try:
        session = current_app.db.session
        user_decoded = token_decoded(request)
        user_id = user_decoded["sub"]["id"]
        data = request.get_json()

        author: UserModel = UserModel.query.filter_by(id=user_id).first()
        user_target: UserModel = UserModel.query.filter_by(id=id).first()

        if not author.group:
            raise InvalidInput("You are not subscribed to any group")

        if not user_target.group:
            raise InvalidInput("target user is not subscribed to any group")

        if not author.group.id == user_target.group.id:
            raise AttributeError

        feedback: FeedbackModel = FeedbackModel(
            event_id=author.event_id, user_id=user_target.id, feedback=data["feedback"])

        session.add(feedback)
        session.commit()

        return jsonify({
            "id": feedback.id,
            "feedback": feedback.feedback,
            "user": {"id": feedback.user_id, "name": feedback.user.name},
            "event": {"id": feedback.event_id, "name": feedback.event.name}
        }), 201
    except AttributeError:
        return jsonify({"msg": "You are not allowed to give feedback to users from other groups"}), 400
    except InvalidInput as e:
        return jsonify(*e.args), 400
    except (TypeError, KeyError):
        return jsonify({"msg": "Expected key 'feedback' with your comment about the target user"}), 400


@jwt_required()
def read_feedbacks(id):
    try:
        if not verify_owner(request, UserModel, id):
            if not verify_owner(request, AdminModel):
                raise PermissionError

        user: UserModel = UserModel.query.filter_by(id=id).first_or_404()

        return jsonify({
            "feedbacks": user.feedback
        })
    except PermissionError:
        return jsonify({"msg": "Only the administrator has access to feedback from another user"}), 401


def generate_report_user(id_user):
    try:

        user: UserModel = UserModel.query.filter_by(id=id_user).first_or_404()

        if not user.feedback:
            feedbacks = []
        else:
            feedbacks = [feed.feedback for feed in user.feedback]

        generate_pdf(user.name, user.email, user.points, feedbacks)

        name = user.name.split(' ')[0]

        return send_file(f'/tmp/{name}.pdf')

    except NotFound:
        return jsonify({"msg": "user not found"}), 404
