import boto3
from boto3.dynamodb.conditions import Key
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


def query(user, pq):
    if pq is None:
        # Returns all data for UI
        return query_all(user)

    assert isinstance(pq, str)
    if pq.endswith('/'):
        name, parent = pq[:-1], pq
        # Returns all data for UI
        return query_item(user, name) + query_children(user, parent)
    else:
        name, parent = pq, f'{pq}/'
        # Returns only 'p' if exists, children for UI otherwise
        return query_item(user, name) or query_children(user, parent)


def query_all(user):
    key = Key('owner').eq(user)
    res = items.query(KeyConditionExpression=key)
    return res.get('Items', [])


def query_item(user, name):
    key = {'owner': user, 'name': name}
    res = items.get_item(Key=key)
    item = res.get('Item', None)
    return ([item] if item is not None else [])


def query_children(user, parent):
    cond = (Key('owner').eq(user) &
            Key('name').begins_with(parent))
    res = items.query(KeyConditionExpression=cond)
    return res.get('Items', [])
