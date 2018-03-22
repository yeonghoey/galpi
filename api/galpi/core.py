from flask import current_app
import requests


def config(name):
    return current_app.config[name]


def exchange(code):
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
