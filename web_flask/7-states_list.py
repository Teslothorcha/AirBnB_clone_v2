from models import storage
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    lis = storage.all("State").values()
    return render_template('7-states_list.html', lis=lis)


@app.teardown_appcontext
def shutdown_(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
