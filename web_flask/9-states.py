#!/usr/bin/python3
""" task 8 """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    states = storage.all("State")
    if id is None:
        return render_template(
            '9-states.html',
            states=storage.all('State').values(),
            len=len(states)
        )
    key = "State.{}".format(id)
    states = states[key] if key in states.keys() else None
    return render_template(
        '9-states.html',
        states=states,
        len=1
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
