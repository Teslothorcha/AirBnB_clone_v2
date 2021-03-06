#!/usr/bin/python3
from models import storage
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    lis = storage.all("State").values()
    return render_template('7-states_list.html', lis=lis)


@app.route('/cities_by_states')
def cities_states():
    st = storage.all('State').values()
    return render_template('8-cities_by_states.html', st=st)


@app.teardown_appcontext
def shutdown_(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
