from flask import Flask, session
from flask_cors import CORS

from galpi.blueprints import root, auth


def create_app():
    app = Flask('galpi')
    app.config.from_object('galpi.config')

    app.register_blueprint(root.bp)
    app.register_blueprint(auth.bp, url_prefix='/auth')

    CORS(app, origins=app.config['CORS_ORIGIN'], supports_credentials=True)

    @app.before_request
    def before_request():
        session.permanent = True

    return app
