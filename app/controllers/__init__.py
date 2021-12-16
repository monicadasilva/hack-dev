from flask_jwt_extended import decode_token
from app.exceptions.exceptions import InvalidInput, InvalidKey
import string
import secrets


def verify(data):

    exepected_keys = ['name', 'email', 'password']
    data_keys = data.keys()
    wrong_keys = list(filter(lambda x: x not in data_keys, exepected_keys))
    invalid_values = []

    for values in data.values():
        if type(values) != str:
            invalid_values.append(values)

    if invalid_values:
        raise InvalidInput({'error': 'All fields must be a string.'})

    if wrong_keys:
        raise InvalidKey({'error': 'Only name, email and password keys are allowed'})

    return ''


def verify_prizes(data):

    exepected_keys = ['name', 'price', 'amount']
    data_keys = data.keys()
    wrong_keys = list(filter(lambda x: x not in data_keys, exepected_keys))

    if wrong_keys:
        raise InvalidKey({'error': 'Only name, price and amount keys are allowed'})

    return ''


def verify_event(data: dict):
    expected_keys = {
        "name": str,
        "description": str,
        "date": str,
        "duration": str,
        "skills": str,
    }
    data_keys = data.keys()
    not_found_key = list(filter(lambda x: x not in data_keys, expected_keys))
    wrong_keys = [key for key in data_keys if key not in list(expected_keys.keys())]
    invalid_values = {}
    valid_values = {}

    if wrong_keys:
        raise InvalidKey({
            'wrong_keys': wrong_keys
        })

    for key, values in data.items():
        if type(values) != expected_keys[key]:
            invalid_values[key] = str(type(values))[8:-2]
            valid_values[key] = str(expected_keys[key])[8:-2]

    if not_found_key:
        raise InvalidKey({
            'not_found_key': not_found_key,
            'expected_keys': list(expected_keys.keys())
        })

    if invalid_values:
        raise InvalidInput({
            'error': 'wrong type of some fields',
            'invalid_values': invalid_values,
            'valid_values': valid_values
        })


def generate_password(comprimento):
    password_characters = string.ascii_letters
    password = ''.join(secrets.choice(password_characters) for i in range(comprimento))
    return password


def token_decoded(request) -> dict:
    token = request.headers["Authorization"][7:]
    return decode_token(token)


def verify_owner(request, Model, id=0) -> bool:

    data_token = token_decoded(request)["sub"]
    query = Model.query.filter_by(email=data_token["email"]).first()

    if id and query:
        if id == query.id:
            return True
        return False

    return bool(query)
