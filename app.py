import os

from flask import Flask, render_template, request
from flask.json import jsonify
import requests


app = Flask('galpi')


CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']


@app.route("/")
def index():
    # TODO: Specify `state`
    return render_template('index.html', client_id=CLIENT_ID)


@app.route("/auth")
def auth():
    url = 'https://github.com/login/oauth/access_token'
    headers = {
        'Accept': 'application/json',
    }
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': request.args['code'],
    }

    res = requests.post(url, headers=headers, data=payload)
    return jsonify(res.json())
