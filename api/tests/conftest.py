import copy
from functools import partial
import json
import pytest
import random


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


@pytest.fixture
def me(monkeypatch):
    def f(user):
        monkeypatch.setattr('galpi.helper.me', lambda: user)
    return f


@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield TestClient(c)


class TestClient():
    def __init__(self, client):
        self.client = client
        self.history = []
        self.last_offset = 0

        for m in ['get',
                  'patch',
                  'post',
                  'head',
                  'put',
                  'delete',
                  'options',
                  'trace']:
            setattr(self, m, partial(self.handle, m))

    def __getitem__(self, last_offset):
        # Just make a shallow copy with last_offset modified
        clone = copy.copy(self)
        clone.last_offset = last_offset
        return clone

    def handle(self, method, *args, **kwargs):
        # Override defaults
        kwargs.setdefault('follow_redirects', True)

        # Custom options
        ok = kwargs.pop('ok', None)
        json_d = kwargs.pop('json', None)

        # werkzeug.test.EnvironBuilder DOES NOT support json.
        # So provide `json` keyword for simplicity.
        if json_d is not None:
            kwargs.setdefault('content_type', 'application/json')
            kwargs.setdefault('data', json.dumps(json_d))

        make_request = getattr(self.client, method)
        response = make_request(*args, **kwargs)
        self.history.append(response)

        if ok is not None:
            if ok:
                assert self.last.status_code < 400
            else:
                assert self.last.status_code >= 400

        return response

    @property
    def last(self):
        return self.history[self.last_offset - 1]

    @property
    def json(self):
        data = self.last.data
        # data can be '' or {}, None, etc.
        if data:
            return json.loads(data)
        else:
            return None

    @property
    def ok(self):
        # As like Response of requests library
        return self.last.status_code < 400

    @property
    def status(self):
        # .status is not compatible with http.HTTPStatus
        return self.last.status_code


@pytest.fixture
def generate_identifier():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
    return lambda k: ''.join(random.choices(chars, k=k))


@pytest.fixture
def user(generate_identifier):
    """Generates a unique user name.

    Since running a single database instance, it is necessary to use unique
    names across tests, othwerwise therer would be some collisions.
    """
    return generate_identifier(16)
