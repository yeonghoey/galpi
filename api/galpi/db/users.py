from galpi.db.tables import users as table
from galpi.db.helper import set_itemattrs


def upsert(username, avatar_url):
    return set_itemattrs(table, key(username), [('avatar_url', avatar_url)])


def get(username):
    res = table.get_item(Key=key(username))
    return res.get('Item', {})


def key(username):
    return {'username': username}
