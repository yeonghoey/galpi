from boto3.dynamodb.conditions import Key

from galpi.db.tables import items as table


def get_all(user):
    k = Key('user').eq(user)
    r = table.query(KeyConditionExpression=k)
    return r.get('Items', [])


def get_item(user, path):
    k = {'user': user, 'path': path}
    r = table.get_item(Key=k)
    return r.get('Item', {})


def put_item(user, path, link):
    table.put_item(Item={
        'user': user,
        'path': path,
        'link': link,
    })
