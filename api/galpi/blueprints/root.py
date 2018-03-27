from flask import Blueprint, jsonify

from galpi.db import get_item, get_user_items
from galpi.github import pass_login


bp = Blueprint('root', __name__)


@bp.route('/')
@pass_login
def index(login):
    return jsonify({'login': login})


@bp.route('/<user>/')
@pass_login
def user(login, user):
    items = get_user_items(user)
    payload = {'user': user, 'items': items}
    return jsonify(payload)


@bp.route('/<user>/<keyword>')
@pass_login
def item(login, user, keyword):
    return jsonify(get_item(user, keyword))
