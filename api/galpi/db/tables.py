from flask import current_app, g
from werkzeug.local import LocalProxy

from galpi.db import db


def table(name):
    def f():
        attr = f'table_{name}'
        if not hasattr(g, attr):
            prefix = current_app.config['TABLE_PREFIX']
            table = db.Table(f'{prefix}-{name}')
            # NOTE: `table.wait_until_exists()` waits 20 seconds by default
            # and expose no parameter. Fall back to the raw client's waiter.
            waiter = db.meta.client.get_waiter('table_exists')
            waiter.wait(TableName=table.name, WaiterConfig={'Delay': 5})
            setattr(g, attr, table)
        return getattr(g, attr)
    return f


items = LocalProxy(table('items'))
