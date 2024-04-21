#!/usr/bin/python3

"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cRoute(text):
    """returns c with the text after"""
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python/<text>', strict_slashes=False)
def pyRoute(text):
    """returns c with the text after"""
    if not text:
        text = "is cool"
    text = text.replace('_', ' ')
    return "Python " + text    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
