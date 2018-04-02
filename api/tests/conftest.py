import os
import sys

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
    child = pexpect.spawn(sls, ['dynamodb', 'start', '--stage', 'dev'])
    child.timeout = None
    child.logfile = sys.stdout
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


@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield c
