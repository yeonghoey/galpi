from http import HTTPStatus

from flask import (
    Blueprint, current_app, jsonify, redirect, request, session, url_for)

from galpi import github


bp = Blueprint('auth', __name__)


@bp.route('/signin')
def signin():
    redirect_uri = url_for('.exchange', _external=True)
    uri, state = github.auth_uri(redirect_uri)
    session['state'] = state
    session['referrer'] = request.headers.get('Referer')
    return redirect(uri)


@bp.route('/exchange')
def exchange():
    code = request.args.get('code')
    state_passed = request.args.get('state')
    state = session.pop('state', None)
    referrer = session.pop('referrer', None)

    if state_passed != state:
        # TODO: handle this properly
        return None

    # TODO: handle error
    token = github.acquire_token(code)
    session['token'] = token

    if referrer is not None:
        return redirect(referrer)
    else:
        return redirect(current_app.config['CORS_ORIGIN'])


@bp.route('/me')
def me():
    token = session.get('token')
    info = github.validate_token(token)
    if info is None:
        session.pop('user', None)
        return jsonify({})
    else:
        user = info.get('user')
        session['user'] = user
        return jsonify(info)


@bp.route('/signout', methods=['POST'])
def signout():
    session.pop('user', None)
    token = session.pop('token', None)

    if token is not None:
        github.revoke_token(token)

    return ('', HTTPStatus.NO_CONTENT)
