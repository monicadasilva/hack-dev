from flask import request, current_app, jsonify
from app.controllers import verify
from app.exceptions.exceptions import InvalidInput, InvalidKey
from sqlalchemy.exc import IntegrityError
from app.models.company_model import CompanyModel
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import NotFound


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