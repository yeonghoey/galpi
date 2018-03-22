import os

from flask import Flask, redirect, render_template, request, session, url_for
import requests


CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
SECRET_KEY = os.environ['SECRET_KEY']


app = Flask('galpi')
app.secret_key = SECRET_KEY


@app.before_request
def before_request():
    session.permanent = True


@app.route("/")
def index():
    # TODO: Specify `state`
    return render_template('index.html', client_id=CLIENT_ID)


@app.route("/auth")
def auth():
    code = request.args['code']
    access_token = exchange(code)
    session['access_token'] = access_token
    return redirect(url_for('index'))


def exchange(code):
    url = 'https://github.com/login/oauth/access_token'

    headers = {
        'Accept': 'application/json',
    }

    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
    }

    res = requests.post(url, headers=headers, data=payload)

    try:
        res.raise_for_status()
    except request.HTTPError:
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
