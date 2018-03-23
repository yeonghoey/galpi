from flask import current_app


def config(name):
    return current_app.config[name]
