#!/usr/bin/python3
from models import storage
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states_list')
def states_list():
    lis = storage.all("State").values()
    return render_template('7-states_list.html', lis=lis)


@app.route('/cities_by_states')
def cities_states():
    st = storage.all('State').values()
    return render_template('8-cities_by_states.html', st=st)


@app.route('/states/<string:id>')
def cit_b_st(id):
    lis = storage.all('State')
    if "State." + id in lis:
        state = lis["State." + id]
    else:
        state = None
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def shutdown_(self):
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    amenities = storage.all('Amenity').values()
    states = storage.all('State').values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
