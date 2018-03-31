from flask import Flask, session
from flask_cors import CORS

from galpi.blueprints import root, auth


def create_app(mapping=None):
    app = Flask('galpi')

    app.config.from_object('galpi.config')
    if mapping is not None:
        app.config.from_mapping(mapping)

    app.register_blueprint(root.bp)
    app.register_blueprint(auth.bp, url_prefix='/auth')

    CORS(app, origins=app.config['CORS_ORIGIN'], supports_credentials=True)

    @app.before_request
    def before_request():
        session.permanent = True

    return app
