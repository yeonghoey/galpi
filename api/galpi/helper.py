from flask import session

from galpi.github import validate_token


def me():
    token = session.get('token')
    if token is None:
        return None
    info = validate_token(token)
    return info.get('user')
