#!/usr/bin/python3
"""
It creates a Flask instance, and then routes the root URL to the
function index()

:param strict_slashes: If set to True, the trailing slashes in a
 route will be, defaults to False
(optional)
:return: The return value of the function is being returned.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index(strict_slashes=False):
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb(strict_slashes=False):
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
