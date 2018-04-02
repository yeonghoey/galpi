import os
from signal import SIGINT
from subprocess import Popen, PIPE

import pytest

from galpi import create_app


@pytest.fixture(scope='session', autouse=True)
def dynamodb():
    proc = start_dynamodb()
    yield
    stop_dynamodb(proc)


def start_dynamodb():
    sls = os.path.join(pytest.config.rootdir, 'node_modules/.bin/sls')
    proc = Popen([sls, 'dynamodb', 'start', '--stage', 'dev'],
                 stdout=PIPE,
                 start_new_session=True)

    # Depend on serverless-dynamodb-local's migration feature.
    # It prints out lines like 'Serverless: DynamoDB - created table <table>'
    # So, just wait for some of the message to show up.
    for bs in proc.stdout:
        line = bs.decode()
        if 'created table' in line:
            break
    return proc


def stop_dynamodb(proc):
    # sls dynamodb creates several subprocesses.
    # To stop all of them, send the signal to the process group.
    pgid = os.getpgid(proc.pid)
    os.killpg(pgid, SIGINT)

    # Ensure that it completely ends
    proc.communicate()


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
