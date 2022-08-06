from http import HTTPStatus
import jwt

from functools import wraps
from flask import request, g  # ! Import request and global 'g' from flask
from models.user import UserModel
from config.environment import secret


def secure_route(route_func):
    @wraps(route_func)
    def decorated_function(*args, **kwargs):
        # ! Doing secure route specific stuff to validate my token
        raw_token = request.headers.get("Authorization")
        # ! Checking token exists
        if not raw_token:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        # ! Clean up token
        clean_token = raw_token.replace("Bearer ", "")

        try:
            # ! Decode the token. It will throw an exception if it is invalid
            payload = jwt.decode(clean_token, secret, "HS256")
            # ! get the user information from the token
            user_id = payload["sub"]
            # ! Get the user model from the id
            user = UserModel.query.get(user_id)

            if not user:
                return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

            # ! Setting current_user as a global variable, so I can access it in my controllers
            g.current_user = user

        # ! this will happen when token is invalid
        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED

        except Exception as e:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        return route_func(*args, **kwargs)

    return decorated_function
