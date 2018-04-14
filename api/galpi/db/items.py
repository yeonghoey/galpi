from boto3.dynamodb.conditions import Key

from galpi.db.tables import items as table
from galpi.helper import ensure_pathkey


def query(username, pathquery):
    self_ = ({} if pathquery is None else
             _get_item(username, pathquery))

    redirect = (pathquery is not None and
                not pathquery.endswith('/')
                and 'linkto' in self_)

    children = (_get_all(username) if pathquery is None else
                _get_children(username, pathquery) if not redirect else
                [])

    return {
        'self': self_,
        'redirect': redirect,
        'children': children,
    }


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
    return _put_item(item)


def _get_all(username):
    key = Key('username').eq(username)
    res = table.query(KeyConditionExpression=key)
    return res.get('Items', [])


def _get_item(username, pathquery):
    pathkey = ensure_pathkey(pathquery)
    key = {'username': username, 'pathkey': pathkey}
    res = table.get_item(Key=key)
    return res.get('Item', {})


def _get_children(username, pathquery):
    pathkey = ensure_pathkey(pathquery)
    cond = (Key('username').eq(username) &
            Key('pathkey').begins_with(f'{pathkey}/'))
    res = table.query(KeyConditionExpression=cond)
    return res.get('Items', [])


def _put_item(item):
    response = table.put_item(Item=item)
    return response
