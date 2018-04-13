from flask import Blueprint, jsonify, redirect, request, session, url_for

from galpi.github import prepare_auth_request, acquire_token, acquire_userinfo


bp = Blueprint('auth', __name__)


@bp.route('/')
def index():
    redirect_uri = url_for('.exchange', _external=True)
    uri, state = prepare_auth_request(redirect_uri)

    session['state'] = state
    return redirect(uri)


@bp.route('/exchange')
def exchange():
    state_passed = request.args['state']
    state = session.pop('state', None)
    if state_passed != state:
        # TODO: handle this properly
        return None

    code = request.args.get('code')
    access_token = acquire_token(code)
    session['access_token'] = access_token

    # TODO: redirect to frontend
    return redirect(url_for('root.home'))


@bp.route('/me')
def me():
    access_token = session.get('access_token')
    if access_token is None:
        return jsonify({})
    else:
        userinfo = acquire_userinfo(access_token)
        session['userinfo'] = userinfo
    return jsonify(userinfo)
