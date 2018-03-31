from flask import Blueprint, jsonify, session

from galpi.db.items import query


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    login = session.get('login')
    return jsonify({'login': login})


@bp.route('/<user>/', defaults={'pq': None})
@bp.route('/<user>/<path:pq>')
def lookup(user, pq):
    payload = query(user, pq)
    return jsonify(payload)
