from collections import defaultdict
from http import HTTPStatus
import re

from flask import abort, Blueprint, jsonify, request, session

from galpi.db import items
from galpi.github import validate_token


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    return ('', HTTPStatus.NO_CONTENT)


@bp.route('/<user>/')
def get_all(user):
    subs = items.get_all(user)
    return jsonify(compose(user, None, subs))


@bp.route('/<user>/<path:path>')
def get_item(user, path):
    path = path.strip('/')
    item = items.get_item(user, path)

    if items.is_link(item):
        base = [user, path]
        link = item['link']
        return jsonify({'base': base, 'link': link})
    elif items.is_folder(item):
        subs = items.get_subs(user, path)
        return jsonify(compose(user, path, subs))
    else:
        abort(HTTPStatus.NOT_FOUND)


@bp.route('/<user>/<path:path>', methods=['PUT'])
def put_item(user, path):
    if me() != user:
        abort(HTTPStatus.FORBIDDEN)

    path = path.strip('/')
    if not validate_path(path):
        abort(HTTPStatus.BAD_REQUEST)
    json = request.get_json()
    link = json and json.get('link')

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
        new_is_folder = link is None
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
        subs = items.get_subs(user, path)
        if subs:
            abort(HTTPStatus.CONFLICT)

    items.delete_item(user, path)
    return ('', HTTPStatus.NO_CONTENT)


def me():
    user = session.get('user')
    if user is not None:
        return user

    token = session.get('token')
    if token is None:
        return None

    info = validate_token(token)
    return info.get('user')


def compose(user, path, subs):
    def tree():
        return defaultdict(tree)

    base = ([user] if path is None else
            [user] + path.split('/'))
    prefix = f'{path}/' if path is not None else ''
    payload = tree()
    payload['base'] = base
    payload['subs'] = tree()
    for item in subs:
        assert item['user'] == user
        assert item['path'].startswith(prefix)
        subpath = item['path'][len(prefix):]
        segments = subpath.split('/')
        parent = payload
        for s in segments:
            parent = parent['subs'][s]
        if 'link' in item:
            parent['link'] = item['link']
        else:
            parent['subs'] = tree()

    return dict(payload)


def validate_path(path):
    segments = path.split('/')
    pattern = r'^[A-Za-z0-9-_]+$'
    return all(re.match(pattern, s) for s in segments)
