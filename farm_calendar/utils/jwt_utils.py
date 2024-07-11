from django.conf import settings

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

def decode_jwt(token):
    try:
        decoded_token = jwt.decode(token, settings.JWT_SIGNING_KEY, algorithms=[settings.JWT_ALG])
        return decoded_token
    except ExpiredSignatureError:
        return None  # Token has expired
    except InvalidTokenError:
        return None  # Invalid token

def get_token_from_header(request):
    auth_header = request.headers.get('Authorization')
    token = None
    if auth_header is not None:
        token = auth_header.split(" ")[1]  # Assumes 'Bearer <token>'
    return token


def get_user_id_from_token(token):
    decoded_token = decode_jwt(token)
    if decoded_token:
        return decoded_token.get(settings.JWT_USER_ID_FIELD)


def get_user_id_from_jwt_request(request):
    auth_header = request.headers.get('Authorization')
    if auth_header is not None:
        token = auth_header.split(" ")[1]  # Assumes 'Bearer <token>'
        decoded_token = decode_jwt(token)
        if decoded_token:
            return decoded_token.get(settings.JWT_USER_ID_FIELD)
    return None