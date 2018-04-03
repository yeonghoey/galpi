from functools import partial
import json
import os
import sys
import uuid

import pexpect
import pytest

from galpi import create_app


@pytest.fixture(scope='session', autouse=True)
def dynamodb():
    child = start_dynamodb()
    yield
    child.close()


def start_dynamodb():
    sls = os.path.join(pytest.config.rootdir, 'node_modules/.bin/sls')
    child = pexpect.spawn(sls,
                          ['dynamodb', 'start', '--stage', 'dev'],
                          encoding='utf-8',
                          logfile=sys.stdout,
                          timeout=None)
    # Depend on serverless-dynamodb-local's migration feature.
    # It prints out lines like 'Serverless: DynamoDB - created table <table>'
    # So, just wait for some of the message to show up.
    child.expect(r'DynamoDB - created table (.+)')
    return child


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
        make_request = getattr(self.client, method)
        response = make_request(*args, **kwargs)
        payload = json.loads(response.data)
        self.history.append(payload)
        return payload

    @property
    def last(self):
        return self.history[-1]


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
    return uuid.uuid4()
