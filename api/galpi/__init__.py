from flask import Flask, session

from galpi.blueprints import root, auth


app = Flask('galpi')
app.config.from_object('galpi.config')
app.register_blueprint(root.bp)
app.register_blueprint(auth.bp, url_prefix='/auth')


@app.before_request
def before_request():
    session.permanent = True
