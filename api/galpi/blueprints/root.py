from http import HTTPStatus
from flask import Blueprint, jsonify, request

from galpi.db import users, items
from galpi.helper import ensure_pathkey


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    return ('', HTTPStatus.NO_CONTENT)


@bp.route('/<username>/')
def user(username):
    payload = users.get(username)
    # TODO: Filter if current user is not allowed to read
    return jsonify(payload)


# @bp.route('/<username>/<path:pathquery>')
# def query(username, pathquery):
#     payload = items.query(username, pathquery)
#     return jsonify(payload)


# @bp.route('/<username>/<path:pathquery>', methods=['PUT'])
# def put(username, pathquery):
#     pathkey = ensure_pathkey(pathquery)

#     # TODO: auth check
#     payload = request.get_json()
#     linkto = payload['linkto']
#     description = payload.get('description')
#     items.put(username, pathkey, linkto, description)
#     return ('', HTTPStatus.CREATED)
