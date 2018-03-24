from os import environ


# Builtin Configs
SECRET_KEY = environ['SECRET_KEY']

# Custom Configs
CLIENT_ID = environ['CLIENT_ID']
CLIENT_SECRET = environ['CLIENT_SECRET']

IS_OFFLINE = environ.get('IS_OFFLINE') is not None
