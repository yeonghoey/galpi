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
    update_userinfo()

    if referrer is not None:
        return redirect(referrer)
    else:
        return redirect(current_app.config['CORS_ORIGIN'])


@bp.route('/me')
def me():
    userinfo = update_userinfo()
    if userinfo is None:
        return ('', HTTPStatus.NO_CONTENT)
    else:
        return jsonify(userinfo)


@bp.route('/signout', methods=['POST'])
def signout():
    session.pop('userinfo', None)
    token = session.pop('token', None)

    if token is not None:
        github.revoke_token(token)

    return ('', HTTPStatus.NO_CONTENT)


def update_userinfo():
    token = session.get('token')
    if token is None:
        return None
    else:
        user = github.acquire_user(token)
        userinfo = to_userinfo(user)
        session['userinfo'] = userinfo
        return userinfo


def to_userinfo(user):
    return {
        'username': user.get('login'),
        'avatar_url': user.get('avatar_url'),
    }
