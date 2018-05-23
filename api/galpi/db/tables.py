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

            # NOTE: Local DB takes time to create tables.
            # In production, they are already there, so skip this.
            if current_app.config['IS_OFFLINE']:
                wait_until_exists(table, 1)
        return getattr(g, attr)
    return f


def wait_until_exists(table, seconds):
    # NOTE: `table.wait_until_exists()` waits 20 seconds by default
    # and expose no parameter. Fall back to the raw client's waiter.
    waiter = db.meta.client.get_waiter('table_exists')
    waiter.wait(TableName=table.name, WaiterConfig={'Delay': seconds})


items = LocalProxy(table('items'))
