#!/usr/bin/python3
"""
It creates a Flask instance, and then uses the route decorator to tell the instance what URL should
trigger the associated function

:param strict_slashes: If set to True, the URLs generated for this endpoint will have a trailing
slash. Defaults to False, defaults to False (optional)
:return: The function index is being returned.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index(strict_slashes=False):
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
