from flask import Flask


app = Flask('galpi')


@app.route("/")
def hello():
    return "Hello World!"
