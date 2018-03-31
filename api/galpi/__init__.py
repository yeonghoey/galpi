from flask import Flask, session
from flask_cors import CORS

from galpi.blueprints import root, auth
from galpi.config import CORS_ORIGIN, SECRET_KEY


def create_app():
    app = Flask('galpi')

    app.secret_key = SECRET_KEY
    app.register_blueprint(root.bp)
    app.register_blueprint(auth.bp, url_prefix='/auth')
    CORS(app, origins=CORS_ORIGIN, supports_credentials=True)

    @app.before_request
    def before_request():
        session.permanent = True

    return app
