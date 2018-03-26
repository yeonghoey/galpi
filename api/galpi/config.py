from os import environ


# Builtin Configs
SECRET_KEY = environ['SECRET_KEY']

# Custom Configs
CLIENT_ID = environ['CLIENT_ID']
CLIENT_SECRET = environ['CLIENT_SECRET']
CORS_ORIGIN = environ['CORS_ORIGIN']
TABLE_PREFIX = environ['TABLE_PREFIX']

# Development Configs
IS_OFFLINE = environ.get('IS_OFFLINE') is not None
