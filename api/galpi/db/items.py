from boto3.dynamodb.conditions import Key

from galpi.db.tables import items


def put(user, name, to):
    item = {'owner': user, 'name': name, 'to': to}
    response = items.put_item(Item=item)
    return response


def query(user, pq):
    if pq is None:
        return {
            'self': {},
            'children': query_all(user),
        }

    assert isinstance(pq, str)

    if pq.endswith('/'):
        return {
            'self': query_item(user, name=pq[:-1]),
            'children': query_children(user, parent=pq),
        }
    else:
        item = query_item(user, name=pq)
        # Skip to retrieve children if item exists,
        # because the client will be redirected right away.
        children = ([] if item else
                    query_children(user, parent=f'{pq}/'))
        return {'self': item, 'children': children}


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
