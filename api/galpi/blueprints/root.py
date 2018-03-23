from flask import Blueprint, jsonify

from galpi.github import pass_login


bp = Blueprint('root', __name__)


@bp.route('/')
@pass_login
def index(login):
    return jsonify({'login': login})
