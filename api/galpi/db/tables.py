from flask import current_app, g
from werkzeug.local import LocalProxy

from galpi.db import db


def table(name):
    def f():
        attr = f'table_{name}'
        if not hasattr(g, attr):
            prefix = current_app.config['TABLE_PREFIX']
            table = db.Table(f'{prefix}-{name}')
            setattr(g, attr, table)
        return getattr(g, attr)
    return f


items = LocalProxy(table('items'))
