#!/usr/bin/python3
"""
Flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    root directory
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb directory
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_life(text):
    """
    text substitution
    """
    return "C {}".format(text).replace("_", " ")


@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/", defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def py_sub(text):
    """
    More text substitution
    """
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def int_n(n):
    """
    int substitution
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def return_template(n):
    """
    render template
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
