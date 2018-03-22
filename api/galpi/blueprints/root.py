from flask import Blueprint, render_template

from galpi.core import config


bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    # TODO: Specify `state`
    return render_template('index.html', client_id=config('CLIENT_ID'))
