from galpi.db.tables import users as table


def create_if_not_exists(username):
    return _update_user(username)


def get(username):
    return _get_user(username)


def _get_user(username):
    res = table.get_item(Key={'username': username})
    return res.get('Item', {})


def _update_user(username):
    table.update_item(Key={'username': username})
