from flask import Blueprint, jsonify

from galpi.db import get_item
from galpi.github import pass_login


bp = Blueprint('root', __name__)


@bp.route('/')
@pass_login
def index(login):
    return jsonify({'login': login})


@bp.route('/<user>/<keyword>')
@pass_login
def lookup(login, user, keyword):
    return jsonify(get_item(user, keyword))
