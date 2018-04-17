import secrets

from flask import current_app
import requests
from requests.auth import HTTPBasicAuth


def auth_uri(redirect_uri):
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


def validate_token(token):
    response = requests.get(auth_url(token), auth=client_auth())
    json = response.json()
    user = json.get('user', {})
    return {
        'user': user.get('login'),
        'avatar_url': user.get('avatar_url'),
    }


def revoke_token(token):
    res = requests.delete(auth_url(token), auth=client_auth())
    return res.ok


def auth_url(token):
    client_id = current_app.config['CLIENT_ID']
    return ('https://api.github.com/applications'
            f'/{client_id}/tokens/{token}')


def client_auth():
    return HTTPBasicAuth(current_app.config['CLIENT_ID'],
                         current_app.config['CLIENT_SECRET'])
