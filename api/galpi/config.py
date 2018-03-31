from os import environ


# Injected by serverless-wsgi
IS_OFFLINE = environ.get('IS_OFFLINE') is not None

# Builtin Configs
TESTING = environ.get('TESTING', False)

SECRET_KEY = environ['SECRET_KEY']
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = not IS_OFFLINE

# Custom Configs
CLIENT_ID = environ['CLIENT_ID']
CLIENT_SECRET = environ['CLIENT_SECRET']
CORS_ORIGIN = environ['CORS_ORIGIN']
TABLE_PREFIX = environ['TABLE_PREFIX']
