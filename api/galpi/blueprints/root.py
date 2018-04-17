from http import HTTPStatus

from flask import abort, Blueprint, jsonify, request

from galpi.db import items
from galpi.helper import me


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    return ('', HTTPStatus.NO_CONTENT)


@bp.route('/<user>/')
def get_all(user):
    all_ = items.get_all(user)
    return jsonify(all_)


@bp.route('/<user>/<name>')
def get_item(user, name):
    item = items.get_item(user, name)
    return jsonify(item)


@bp.route('/<user>/<name>', methods=['PUT'])
def put_item(user, name):
    if me() != user:
        abort(HTTPStatus.FORBIDDEN)

    json = request.get_json()
    link = json['link']
    items.put_item(user, name, link)
    return ('', HTTPStatus.CREATED)
