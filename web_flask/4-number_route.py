
#!/usr/bin/python3
"""
Flask application
"""

from flask import Flask

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
    """int substitution"""
    return f"{n} is a number"
