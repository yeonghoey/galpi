import boto3
from flask import g
from werkzeug.local import LocalProxy
from galpi.config import IS_OFFLINE, TABLE_PREFIX


def get_db():
    if not hasattr(g, 'db'):
        g.db = make_db()
    return g.db


def make_db():
    if IS_OFFLINE:
        return boto3.resource('dynamodb',
                              region_name='localhost',
                              endpoint_url='http://localhost:8000')
    else:
        return boto3.resource('dynamodb')


db = LocalProxy(get_db)
items = LocalProxy(lambda: db.Table(f'{TABLE_PREFIX}-items'))


def get_item(user, keyword):
    res = items.get_item(Key={'user': user, 'keyword': keyword})
    # TODO: Handle errors and other unexpected cases
    return res.get('Item', {})
