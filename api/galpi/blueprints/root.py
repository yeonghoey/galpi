from http import HTTPStatus

from flask import abort, Blueprint, jsonify, request, session

from galpi.db import items
from galpi.github import validate_token


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    return ('', HTTPStatus.NO_CONTENT)


@bp.route('/<user>/')
def get_all(user):
    all_ = items.get_all(user)
    return jsonify(all_)


@bp.route('/<user>/<path:path>')
def get_item(user, path):
    path = path.strip('/')
    item = items.get_item(user, path)
    return jsonify(item)


@bp.route('/<user>/<path:path>', methods=['PUT'])
def put_item(user, path):
    if me() != user:
        abort(HTTPStatus.FORBIDDEN)
    path = path.strip('/')
    json = request.get_json()
    link = json.get('link')
    items.put_item(user, path, link)
    return ('', HTTPStatus.CREATED)


def me():
    token = session.get('token')
    if token is None:
        return None
    info = validate_token(token)
    return info.get('user')
