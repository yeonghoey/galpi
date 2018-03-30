from flask import Blueprint, jsonify, request, session

from galpi import db


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    login = session.get('login')
    return jsonify({'login': login})


@bp.route('/<user>/', defaults={'pq': None})
@bp.route('/<user>/<path:pq>')
def query(user, pq):
    items = db.query(user, pq)
    payload = {'owner': user, 'items': items}
    return jsonify(payload)
