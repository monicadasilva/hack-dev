from flask import request, current_app, jsonify,redirect, url_for, session
from app.controllers import verify, verify_event
from app.exceptions.exceptions import InvalidInput, InvalidKey
from sqlalchemy.exc import IntegrityError
from app.models.company_model import CompanyModel
from flask_jwt_extended import create_access_token, jwt_required, decode_token
from werkzeug.exceptions import NotFound
from app.configs.google import oauth, google
from app.models.event_model import EventsModel


def create_company():
    session = current_app.db.session
    data = request.get_json()

    try:
        verify(data)
        company = CompanyModel(**data)
        session.add(company)
        session.commit()

        return {
            "id": company.id,
            "name": company.name,
            "email": company.email,
            "avatar": company.avatar,
            "mkt_material": company.mkt_material
        }, 201
    except InvalidInput as e:
        return jsonify(*e.args), 400

    except InvalidKey as e:
        return jsonify(*e.args), 400

    except IntegrityError:
        return {"msg": "This email already registered!"}, 409


def login_company():
    try:
        data = request.get_json()

        company: CompanyModel = CompanyModel.query.filter_by(email=data['email']).first_or_404()

        if company.verify_password(data["password"]):
            token = create_access_token(company)
            return jsonify({
                "token": token,
                "company": {
                    "id": company.id,
                    "name": company.name,
                    "email": company.email
                }
            }), 200
        else:
            return jsonify({"msg": "Incorrect password"}), 400

    except KeyError as e:
        return jsonify({"expected_key": e.args}), 400
    except NotFound:
        return jsonify({"error": "Company not found"}), 404


@jwt_required()
def create_event():
    session = current_app.db.session
    data = request.get_json()
    try:
        verify_event(data)
        token = request.headers["Authorization"][7:]
        data["pending"] = True

        token_company = decode_token(token)["sub"]

        company = CompanyModel.query.filter_by(email=token_company["email"]).first()

        if not company:
            return {"msg": "only registered companies can create events"}, 401

        new_event: EventsModel = EventsModel(**data)
        session.add(new_event)
        session.commit()

        return jsonify({
            "id": new_event.id,
            "name": new_event.name,
            "description": new_event.description,
            "date": new_event.date,
            "duration": new_event.duration,
            "pending": new_event.pending,
            "skill": new_event.skills,
        }), 201

    except InvalidKey as e:
        return jsonify(*e.args), 400

    except InvalidInput as e:
        return jsonify(*e.args), 400


@jwt_required()
def get_one_company(id):
    try:
        company = CompanyModel.query.filter_by(id=id).first_or_404()
        return jsonify(company)

    except NotFound:
        return {"error": "Company not found"}, 404


@jwt_required()
def get_all_companies():
    companies = CompanyModel.query.all()

    return jsonify([{
        "id": company.id,
        "name": company.name,
        "email": company.email,
        "avatar_id": company.avatar_id,
    } for company in companies]), 200


def google_login():
    google = oauth.create_client('google') 
    redirect_uri = url_for('bp_company.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


def authorize():
    dbsession = current_app.db.session
    
    google = oauth.create_client('google')
    token = google.authorize_access_token() 
    resp = google.get('userinfo') 
    user_info = resp.json()
    user = oauth.google.userinfo()  
    
    user_data = {'name': user.name, 'email': user.email}
    user_db = CompanyModel.query.filter_by(email=user.email).first()
    
    if user_db == None:
        new_user = CompanyModel(**user_data)
        dbsession.add(new_user)
        dbsession.commit()
        return jsonify({
                "token": token,
                "user": {
                    "id": new_user.id,
                    "name": new_user.name,
                    "email": new_user.email,
                }
            }), 200
    
    session['profile'] = user_info
    session.permanent = True 
    return redirect('/company/dashboard')


def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')