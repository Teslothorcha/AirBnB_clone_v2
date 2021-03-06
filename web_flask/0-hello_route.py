#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ first route message"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
