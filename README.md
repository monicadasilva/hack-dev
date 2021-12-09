# Project: <HACK_DEV/>

## <Hack_dev/> API collection

This collection contains all requests from the [API](http://)

It contains following requests

\*Users:

- Register
- Login
- Update avatar
- Update address
- Update info
- Get specific user details
- Get all prizes
- Signup envent

\*Admin:

- Register
- Login
- Create prizes
- Update avatar
- Update event

\*Events:

- Get one
- Get all

\*Company:

- Register
- Login
- Create event

# 📁 Collection: User

## End-point: User info

Get specific user info by id

### Method: GET

> ```
> http://localhost:5000/users/1
> ```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                     | Type   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA2ODA5MSwianRpIjoiNzEyMzU3NWQtYWEzYi00MjA5LThmYjgtZTZmMWY2MGQ2NzgxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwicG9pbnRzIjowLCJhdmF0YXJfaWQiOm51bGwsImFkZHJlc3NfaWQiOm51bGwsImV2ZW50X2lkIjpudWxsfSwibmJmIjoxNjM5MDY4MDkxLCJleHAiOjE2NDAzNjQwOTF9.ulm2q--4IjNJhi6r8QuDNTnk-97UcGJusmSdW6N_q8s | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: All Prizes

List all prizes

### Method: GET

> ```
> http://localhost:5000/users/prizes
> ```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                     | Type   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA2ODA5MSwianRpIjoiNzEyMzU3NWQtYWEzYi00MjA5LThmYjgtZTZmMWY2MGQ2NzgxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwicG9pbnRzIjowLCJhdmF0YXJfaWQiOm51bGwsImFkZHJlc3NfaWQiOm51bGwsImV2ZW50X2lkIjpudWxsfSwibmJmIjoxNjM5MDY4MDkxLCJleHAiOjE2NDAzNjQwOTF9.ulm2q--4IjNJhi6r8QuDNTnk-97UcGJusmSdW6N_q8s | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: User Avatar

List all prizes

### Method: GET

> ```
> http://localhost:5000/users/avatar/1
> ```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                     | Type   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA2ODA5MSwianRpIjoiNzEyMzU3NWQtYWEzYi00MjA5LThmYjgtZTZmMWY2MGQ2NzgxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwicG9pbnRzIjowLCJhdmF0YXJfaWQiOm51bGwsImFkZHJlc3NfaWQiOm51bGwsImV2ZW50X2lkIjpudWxsfSwibmJmIjoxNjM5MDY4MDkxLCJleHAiOjE2NDAzNjQwOTF9.ulm2q--4IjNJhi6r8QuDNTnk-97UcGJusmSdW6N_q8s | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: User Register

Register new user

### Method: POST

> ```
> http://localhost:5000/users/signup
> ```

### Body (**raw**)

```json
{
  "name": "Jane Doe",
  "email": "jane@mail.com",
  "password": "123456"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: User Login

### Method: POST

> ```
> http://localhost:5000/users/login
> ```

### Body (**raw**)

```json
{
  "email": "jane@mail.com",
  "password": "13456"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: User Avatar Update

Update user avatar by user id

### Method: PATCH

> ```
> http://localhost:5000/users/update/avatar/1
> ```

### Body formdata

| Param  | value                               | Type |
| ------ | ----------------------------------- | ---- |
| avatar | /home/monica/Downloads/currfoto.png | file |

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                     | Type   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA2ODA5MSwianRpIjoiNzEyMzU3NWQtYWEzYi00MjA5LThmYjgtZTZmMWY2MGQ2NzgxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwicG9pbnRzIjowLCJhdmF0YXJfaWQiOm51bGwsImFkZHJlc3NfaWQiOm51bGwsImV2ZW50X2lkIjpudWxsfSwibmJmIjoxNjM5MDY4MDkxLCJleHAiOjE2NDAzNjQwOTF9.ulm2q--4IjNJhi6r8QuDNTnk-97UcGJusmSdW6N_q8s | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: User Address Update

### Method: PATCH

> ```
> http://localhost:5000/users/address/update/1
> ```

### Body (**raw**)

```json
{
  "street": "rua teste",
  "number": 15,
  "district": "Jd. teste",
  "city": "teste",
  "state": "SP",
  "zip_code": "11432-320"
}
```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                     | Type   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA2ODA5MSwianRpIjoiNzEyMzU3NWQtYWEzYi00MjA5LThmYjgtZTZmMWY2MGQ2NzgxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwicG9pbnRzIjowLCJhdmF0YXJfaWQiOm51bGwsImFkZHJlc3NfaWQiOm51bGwsImV2ZW50X2lkIjpudWxsfSwibmJmIjoxNjM5MDY4MDkxLCJleHAiOjE2NDAzNjQwOTF9.ulm2q--4IjNJhi6r8QuDNTnk-97UcGJusmSdW6N_q8s | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: User Update

### Method: PATCH

> ```
> http://localhost:5000/users/2
> ```

### Body (**raw**)

```json
{
  "name": "Jhon Doe",
  "email": "jhon@mail.com",
  "password": "147258"
}
```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                     | Type   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA2ODA5MSwianRpIjoiNzEyMzU3NWQtYWEzYi00MjA5LThmYjgtZTZmMWY2MGQ2NzgxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwicG9pbnRzIjowLCJhdmF0YXJfaWQiOm51bGwsImFkZHJlc3NfaWQiOm51bGwsImV2ZW50X2lkIjpudWxsfSwibmJmIjoxNjM5MDY4MDkxLCJleHAiOjE2NDAzNjQwOTF9.ulm2q--4IjNJhi6r8QuDNTnk-97UcGJusmSdW6N_q8s | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: User Event signup

### Method: PATCH

> ```
> http://localhost:5000/users/event/signup/1
> ```

### Body (**raw**)

```json
{
  "name": "KenzieHack"
}
```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                        | Type   |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3Mzk1NCwianRpIjoiYWU4YTBjZjYtZTE0Yy00NmYwLThhNDAtZTAwNGMxN2ZkYjdmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lc0BtYWlsLmNvbSIsInBvaW50cyI6MCwiYXZhdGFyX2lkIjpudWxsLCJhZGRyZXNzX2lkIjpudWxsLCJldmVudF9pZCI6bnVsbH0sIm5iZiI6MTYzOTA3Mzk1NCwiZXhwIjoxNjQwMzY5OTU0fQ.\_ea0dThPjWgvS5vt1mAJFfm6lz2Nf6fKlFORFoc4xO4 | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: User Delete

### Method: DELETE

> ```
> http://localhost:5000/users/2
> ```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                     | Type   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA2ODA5MSwianRpIjoiNzEyMzU3NWQtYWEzYi00MjA5LThmYjgtZTZmMWY2MGQ2NzgxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwicG9pbnRzIjowLCJhdmF0YXJfaWQiOm51bGwsImFkZHJlc3NfaWQiOm51bGwsImV2ZW50X2lkIjpudWxsfSwibmJmIjoxNjM5MDY4MDkxLCJleHAiOjE2NDAzNjQwOTF9.ulm2q--4IjNJhi6r8QuDNTnk-97UcGJusmSdW6N_q8s | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📁 Collection: Admin

## End-point: Admin Avatar

List all prizes

### Method: GET

> ```
> http://localhost:5000/admin/avatar/1
> ```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                                                        | Type   |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3Mzk1NCwianRpIjoiYWU4YTBjZjYtZTE0Yy00NmYwLThhNDAtZTAwNGMxN2ZkYjdmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lc0BtYWlsLmNvbSIsInBvaW50cyI6MCwiYXZhdGFyX2lkIjpudWxsLCJhZGRyZXNzX2lkIjpudWxsLCJldmVudF9pZCI6bnVsbH0sIm5iZiI6MTYzOTA3Mzk1NCwiZXhwIjoxNjQwMzY5OTU0fQ.\_ea0dThPjWgvS5vt1mAJFfm6lz2Nf6fKlFORFoc4xO4 | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Admin Register

### Method: POST

> ```
> http://localhost:5000/admin/signup
> ```

### Body (**raw**)

```json
{
  "name": "Jane Doe",
  "email": "jane@mail.com",
  "password": "123456"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Admin Login

### Method: POST

> ```
> http://localhost:5000/admin/login
> ```

### Body (**raw**)

```json
{
  "email": "jane@mail.com",
  "password": "123456"
}
```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                   | Type   |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3MzcwMiwianRpIjoiNDA3NmE3OTQtZWJjMi00ODQ2LWJkMzUtZGI4NzU5NmI4ZTEyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIn0sIm5iZiI6MTYzOTA3MzcwMiwiZXhwIjoxNjQwMzY5NzAyfQ.yPgoeFSc6lpUQ7AIc3eP61ywRaFUfL9BvUvXVdgixaE | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Admin Create Prizes

### Method: POST

> ```
> http://localhost:5000/admin/prizes
> ```

### Body (**raw**)

```json
{
  "name": "keyboard",
  "price": 100,
  "amount": 50
}
```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                   | Type   |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA4MTAzNiwianRpIjoiZjkwZjJkOGUtZTUyMi00NjQzLWJhMzItNzBlMTQxMzk2ZWJlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIn0sIm5iZiI6MTYzOTA4MTAzNiwiZXhwIjoxNjQwMzc3MDM2fQ.2ZRmraJGqIsfLiqAyW8G4gyYo9G3Lw8Ij36w9UP9q08 | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Admin Event Update

### Method: PATCH

> ```
> http://localhost:5000/admin/update/event/1
> ```

### Body (**raw**)

```json
{
  "pending": false
}
```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                   | Type   |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3MzcwMiwianRpIjoiNDA3NmE3OTQtZWJjMi00ODQ2LWJkMzUtZGI4NzU5NmI4ZTEyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIn0sIm5iZiI6MTYzOTA3MzcwMiwiZXhwIjoxNjQwMzY5NzAyfQ.yPgoeFSc6lpUQ7AIc3eP61ywRaFUfL9BvUvXVdgixaE | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Admin Avatar Update

### Method: PATCH

> ```
> http://localhost:5000/users/update/1
> ```

### Body formdata

| Param | value | Type |
| ----- | ----- | ---- |
|       |       | file |

### 🔑 Authentication bearer

| Param | value | Type |
| ----- | ----- | ---- |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📁 Collection: Events

## End-point: One Event

### Method: GET

> ```
> http://localhost:5000/events/1
> ```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                    | Type   |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3MzQyNCwianRpIjoiYmM2MzAxNjktMDMwMC00YTYxLTk5NDgtODQzNGQyOTU1ZTgzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwiYXZhdGFyX2lkIjpudWxsLCJta3RfbWF0ZXJpYWwiOm51bGx9LCJuYmYiOjE2MzkwNzM0MjQsImV4cCI6MTY0MDM2OTQyNH0.Y7AXqsRPnpWZRR_iMZqj3slo668-aiH0BDfZHMDEBw8 | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: All Events

### Method: GET

> ```
> http://localhost:5000/events
> ```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                                                                    | Type   |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3MzQyNCwianRpIjoiYmM2MzAxNjktMDMwMC00YTYxLTk5NDgtODQzNGQyOTU1ZTgzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIiwiYXZhdGFyX2lkIjpudWxsLCJta3RfbWF0ZXJpYWwiOm51bGx9LCJuYmYiOjE2MzkwNzM0MjQsImV4cCI6MTY0MDM2OTQyNH0.Y7AXqsRPnpWZRR_iMZqj3slo668-aiH0BDfZHMDEBw8 | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📁 Collection: Company

## End-point: Company Register

### Method: POST

> ```
> http://localhost:5000/company/signup
> ```

### Body (**raw**)

```json
{
  "name": "Jane Doe",
  "email": "jane@mail.com",
  "password": "123456"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Company Login

### Method: POST

> ```
> http://localhost:5000/company/login
> ```

### Body (**raw**)

```json
{
  "email": "jane@mail.com",
  "password": "123456"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Company Create Event

### Method: POST

> ```
> http://localhost:5000/company/events
> ```

### Body (**raw**)

```json
{
  "name": "KenzieHack",
  "date": "24/01/2022",
  "duration": "26/01/2022",
  "description": "alguma coisa",
  "skills": "[testes, teste]"
}
```

### 🔑 Authentication bearer

| Param | value                                                                                                                                                                                                                                                                                                                                   | Type   |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| token | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA4MTAzNiwianRpIjoiZjkwZjJkOGUtZTUyMi00NjQzLWJhMzItNzBlMTQxMzk2ZWJlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkphbmUgRG9lIiwiZW1haWwiOiJqYW5lQG1haWwuY29tIn0sIm5iZiI6MTYzOTA4MTAzNiwiZXhwIjoxNjQwMzc3MDM2fQ.2ZRmraJGqIsfLiqAyW8G4gyYo9G3Lw8Ij36w9UP9q08 | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

---

Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
