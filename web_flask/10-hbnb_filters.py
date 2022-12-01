#!/usr/bin/python3
""" task 8 """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Render a particular state """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template(
        '10-hbnb_filters.html',
        states=states, amenities=amenities
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
