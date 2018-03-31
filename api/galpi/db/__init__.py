import boto3
from flask import current_app, g
from werkzeug.local import LocalProxy


def get_db():
    if not hasattr(g, 'db'):
        g.db = make_db()
    return g.db


def make_db():
    if current_app.config['IS_OFFLINE']:
        return boto3.resource('dynamodb',
                              region_name='localhost',
                              endpoint_url='http://localhost:8000')
    else:
        return boto3.resource('dynamodb')


db = LocalProxy(get_db)
