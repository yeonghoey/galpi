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
    if items.is_folder(item):
        ds = items.get_descendants(user, path)
        return jsonify(ds)
    else:
        return jsonify(item)


@bp.route('/<user>/<path:path>', methods=['PUT'])
def put_item(user, path):
    if me() != user:
        abort(HTTPStatus.FORBIDDEN)

    path = path.strip('/')
    json = request.get_json()
    link = json.get('link')

    # if dirname exists, it must be a folder
    dirname, _, basename = path.rpartition('/')
    if dirname:
        parent = items.get_item(user, dirname)
        if not items.is_folder(parent):
            abort(HTTPStatus.CONFLICT)

    # Updating is only allowd for same types
    old = items.get_item(user, path)
    is_update = bool(old)
    if is_update:
        old_is_folder = items.is_folder(old)
        new_is_folder = bool(link is None)
        if old_is_folder != new_is_folder:
            abort(HTTPStatus.CONFLICT)

    items.put_item(user, path, link)
    status = (HTTPStatus.NO_CONTENT if is_update else
              HTTPStatus.CREATED)
    return ('', status, {'Content-Location': request.path})


@bp.route('/<user>/<path:path>', methods=['DELETE'])
def delete_item(user, path):
    if me() != user:
        abort(HTTPStatus.FORBIDDEN)

    path = path.strip('/')
    item = items.get_item(user, path)

    # If the item is a folder, it must be empty
    if items.is_folder(item):
        ds = items.get_descendants(user, path)
        if ds:
            abort(HTTPStatus.CONFLICT)

    items.delete_item(user, path)
    return ('', HTTPStatus.NO_CONTENT)


def me():
    token = session.get('token')
    if token is None:
        return None
    info = validate_token(token)
    return info.get('user')
