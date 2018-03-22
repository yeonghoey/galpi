import os


def declare(name):
    globals()[name] = os.environ[name]


# Builtin Configs
declare('SECRET_KEY')

# Custom Configs
declare('CLIENT_ID')
declare('CLIENT_SECRET')
