from flask import Blueprint, redirect, request, session, url_for

from galpi.github import prepare_auth_request, acquire_token


bp = Blueprint('auth', __name__)


@bp.route('/')
def index():
    redirect_uri = url_for('.exchange', _external=True)
    uri, state = prepare_auth_request(redirect_uri)

    session['state'] = state
    return redirect(uri)


@bp.route('/exchange')
def exchange():
    state = request.args.get('state')
    if state != session['state']:
        # TODO: handle this properly
        return None

    code = request.args.get('code')
    access_token = acquire_token(code)

    session['access_token'] = access_token
    return redirect(url_for('root.index'))
