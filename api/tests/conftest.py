from functools import partial
import json
import os
import sys
import uuid

import pytest

from galpi import create_app


@pytest.fixture
def app(monkeypatch):
    env = {
        'IS_OFFLINE': True,
        'TESTING': True,
        'SECRET_KEY': '<secret>',
        'CLIENT_ID': '',
        'CLIENT_SECRET': '',
        'CORS_ORIGIN': '',
        'TABLE_PREFIX': 'galpi-dev',
    }

    for name, value in env.items():
        monkeypatch.setenv(name, value)

    app = create_app()
    yield app


class TestClient():
    def __init__(self, client):
        self.client = client
        self.history = []

        for m in ['get',
                  'patch',
                  'post',
                  'head',
                  'put',
                  'delete',
                  'options',
                  'trace']:
            setattr(self, m, partial(self.handle, m))

    def handle(self, method, *args, **kwargs):
        kwargs.setdefault('follow_redirects', True)

        # werkzeug.test.EnvironBuilder DOES NOT support json.
        # So provide `json` keyword for simplicity.
        json_d = kwargs.pop('json', None)
        if json_d is not None:
            kwargs.setdefault('content_type', 'application/json')
            kwargs.setdefault('data', json.dumps(json_d))

        make_request = getattr(self.client, method)
        response = make_request(*args, **kwargs)
        self.history.append(response)
        return response

    @property
    def last(self):
        return self.history[-1]

    @property
    def json(self):
        data = self.last.data
        # data can be '' or {}, None, etc.
        if data:
            return json.loads(data)
        else:
            return None

    @property
    def status(self):
        return self.last.status_code


@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield TestClient(c)


@pytest.fixture
def user():
    """Generates a unique user name.

    Since running a single database instance, it is necessary to use unique
    names across tests, othwerwise therer would be some collisions.
    """
    # TODO: Adapt when implements user name patterns and rules
    return str(uuid.uuid4())
