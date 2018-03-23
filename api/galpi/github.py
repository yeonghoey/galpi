import secrets

import requests

from galpi.core import config


def prepare_auth_request():
    url = 'https://github.com/login/oauth/authorize'

    state = secrets.token_urlsafe(16)
    payload = {
        'client_id': config('CLIENT_ID'),
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
        'client_id': config('CLIENT_ID'),
        'client_secret': config('CLIENT_SECRET'),
        'code': code,
    }

    res = requests.post(url, headers=headers, data=payload)

    try:
        res.raise_for_status()
    except requests.HTTPError:
        # TODO: Handle error properly
        return None

    try:
        d = res.json()
    except ValueError:
        # TODO: Handle error properly
        return None

    try:
        return d['access_token']
    except KeyError:
        # TODO: Handle error properly
        return None
