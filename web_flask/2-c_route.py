#!/usr/bin/python3
"""
"The function C_is_fun()
returns a string that is the concatenation of the string "C " and the value of
the variable text with underscores (_) replaced by spaces ( )."

:param strict_slashes: If set to True, the strict_slashes parameter will cause a 404 Not Found error
to be raised if a url that requires a trailing slash is accessed without one, defaults to False
(optional)
:return: The route is being returned.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index(strict_slashes=False):
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb(strict_slashes=False):
    return "HBNB"


@app.route('/c/<text>')
def C_is_fun(text, strict_slashes=False):
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
