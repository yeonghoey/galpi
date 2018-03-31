import secrets

from flask import current_app
import requests
from requests.auth import HTTPBasicAuth


def prepare_auth_request(redirect_uri):
    url = 'https://github.com/login/oauth/authorize'
    state = secrets.token_urlsafe(16)
    payload = {
        'client_id': current_app.config['CLIENT_ID'],
        'redirect_uri': redirect_uri,
        'state': state,
    }

    # Use requests to build URI
    req = requests.Request('GET', url, params=payload)
    req = req.prepare()
    return (req.url, state)


def acquire_token(code):
    url = 'https://github.com/login/oauth/access_token'
    headers = {
        'Accept': 'application/json',
    }
    payload = {
        'client_id': current_app.config['CLIENT_ID'],
        'client_secret': current_app.config['CLIENT_SECRET'],
        'code': code,
    }

    res = requests.post(url, headers=headers, data=payload)

    return res.json()['access_token']


def acquire_login(access_token):
    url_fmt = 'https://api.github.com/applications/%s/tokens/%s'
    url = url_fmt % (current_app.config['CLIENT_ID'], access_token)

    res = requests.get(url, auth=client_auth())

    user = res.json().get('user', {})
    return user.get('login')


def client_auth():
    return HTTPBasicAuth(current_app.config['CLIENT_ID'],
                         current_app.config['CLIENT_SECRET'])
