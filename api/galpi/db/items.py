from boto3.dynamodb.conditions import Key

from galpi.db.tables import items as table


def get_all(user):
    c = Key('user').eq(user)
    r = table.query(KeyConditionExpression=c)
    return r.get('Items', [])


def get_item(user, path):
    k = {'user': user, 'path': path}
    r = table.get_item(Key=k)
    return r.get('Item', {})


def get_subs(user, path):
    c = (Key('user').eq(user) &
         Key('path').begins_with(f'{path}/'))
    r = table.query(KeyConditionExpression=c)
    return r.get('Items', [])


def is_folder(item):
    return bool(item and item.get('link') is None)


def put_item(user, path, link):
    table.put_item(Item={'user': user, 'path': path, 'link': link})


def delete_item(user, path):
    k = {'user': user, 'path': path}
    table.delete_item(Key=k)
