from flask import request, current_app, jsonify
from werkzeug.utils import secure_filename
from app.controllers import verify
from app.exceptions.exceptions import InvalidInput, InvalidKey
from app.models.admin_model import AdminModel
from app.models.avatar_model import AvatarModel
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token
from sqlalchemy import exc
from werkzeug.exceptions import NotFound
from flask_jwt_extended import jwt_required


def login_admin():
    try:
        data = request.get_json()

        admin: AdminModel = AdminModel.query.filter_by(email=data['email']).first_or_404()

        if admin.verify_password(data["password"]):
            token = create_access_token(admin)
            return jsonify({
                "token": token,
                "admin": {
                    "id": admin.id,
                    "name": admin.name,
                    "email": admin.name
                }
            }), 200
        else:
            return jsonify({"msg": "Incorrect password"}), 400

    except KeyError as e:
        return jsonify({"expected_key": e.args}), 400
    except NotFound:
        return jsonify({"error": "Admin not found"}), 404


def create_admin():
    session = current_app.db.session
    #name - email - password
    data = request.get_json()

    try:
        verify(data)
        admin = AdminModel(**data)
        session.add(admin)
        session.commit()

        return {"id": admin.id, "name": admin.name, "email": admin.email}, 201
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

    AdminModel.query.filter_by(id=id).update({'avatar_id': img.id})
    session.commit()

    return '', 204