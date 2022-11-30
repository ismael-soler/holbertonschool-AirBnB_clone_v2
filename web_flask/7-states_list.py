#!/usr/bin/python3
""" ni idea """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ renders all states """

    return render_template('7-states_list.html', states=storage.all("State").values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
