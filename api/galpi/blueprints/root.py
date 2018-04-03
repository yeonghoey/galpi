from http import HTTPStatus
from flask import Blueprint, jsonify, session

from galpi.db import items


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    login = session.get('login')
    return jsonify({'login': login})


@bp.route('/<user>/', defaults={'pq': None})
@bp.route('/<user>/<path:pq>')
def lookup(user, pq):
    payload = items.query(user, pq)
    return jsonify(payload)


@bp.route('/<user>/<path:name>', methods=['PUT'])
def add_item(user, name):
    items.put(user, name, 'A')
    return ('', HTTPStatus.CREATED)
