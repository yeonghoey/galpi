from flask import Blueprint


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    return 'Hello galpi'
