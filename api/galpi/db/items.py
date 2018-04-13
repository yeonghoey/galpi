from boto3.dynamodb.conditions import Key

from galpi.db.tables import items as table
from galpi.helper import ensure_pathkey


def put(username,
        pathkey,
        linkto,
        description):
    item = {
        'username': username,
        'pathkey': pathkey,
        'linkto': linkto,
        'description': description,
    }
    response = table.put_item(Item=item)
    return response


def query(username, pathquery):
    if pathquery is None:
        return {
            'self': {},
            'children': query_all(username),
        }

    item = query_item(username, pathquery)
    children_needed = (pathquery.endswith('/') or (not item))
    children = (query_children(username, pathquery) if children_needed else [])

    return {
        'self': item,
        'children': children,
    }


def query_all(username):
    key = Key('username').eq(username)
    res = table.query(KeyConditionExpression=key)
    return res.get('Items', [])


def query_item(username, pathquery):
    pathkey = ensure_pathkey(pathquery)
    key = {'username': username, 'pathkey': pathkey}
    res = table.get_item(Key=key)
    return res.get('Item', {})


def query_children(username, pathquery):
    pathkey = ensure_pathkey(pathquery)
    cond = (Key('username').eq(username) &
            Key('pathkey').begins_with(f'{pathkey}/'))
    res = table.query(KeyConditionExpression=cond)
    return res.get('Items', [])
