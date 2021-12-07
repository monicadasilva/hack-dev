from app.exceptions.exceptions import InvalidInput, InvalidKey


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
