from flask import (
    Blueprint, redirect, render_template, request, session, url_for)

from galpi.core import config, exchange


bp = Blueprint('auth', __name__)


@bp.route('/')
def github_request():
    # TODO: Specify `state`
    return render_template('index.html', client_id=config('CLIENT_ID'))


@bp.route('/exchange')
def github_exchange():
    code = request.args['code']
    access_token = exchange(code)
    session['access_token'] = access_token
    return redirect(url_for('root.index'))
