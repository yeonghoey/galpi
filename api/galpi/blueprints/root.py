from http import HTTPStatus
from flask import Blueprint, jsonify, request

from galpi.db import items


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    return ('', HTTPStatus.NO_CONTENT)


@bp.route('/<user>/', defaults={'pq': None})
@bp.route('/<user>/<path:pq>')
def query(user, pq):
    payload = items.query(user, pq)
    return jsonify(payload)


@bp.route('/<user>/<path:pq>', methods=['PUT'])
def put(user, pq):
    name = pq.strip('/')

    # TODO: auth check
    payload = request.get_json()
    to = payload['to']
    items.put(user, name, to)
    return ('', HTTPStatus.CREATED)
