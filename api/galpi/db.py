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
        return {
            'item': {},
            'children': query_all(user),
        }

    assert isinstance(pq, str)

    if pq.endswith('/'):
        return {
            'item': query_item(user, name=pq[:-1]),
            'children': query_children(user, parent=pq),
        }
    else:
        item = query_item(user, name=pq)
        # Skip to retrieve children if item exists,
        # because the client will be redirected right away.
        children = ([] if item else
                    query_children(user, parent=f'{pq}/'))
        return {'item': item, 'children': children}


def query_all(user):
    key = Key('owner').eq(user)
    res = items.query(KeyConditionExpression=key)
    return res.get('Items', [])


def query_item(user, name):
    key = {'owner': user, 'name': name}
    res = items.get_item(Key=key)
    return res.get('Item', {})


def query_children(user, parent):
    cond = (Key('owner').eq(user) &
            Key('name').begins_with(parent))
    res = items.query(KeyConditionExpression=cond)
    return res.get('Items', [])
