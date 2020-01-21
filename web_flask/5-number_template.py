#!/usr/bin/python3
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ first route message"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """ second route message"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ third route message"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ third route message"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def python_is_int(n):
    """ third route message"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def first_render(n):
    """ third route message"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run()
