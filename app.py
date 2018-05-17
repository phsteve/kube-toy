import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'wow it works'

@app.route('/healthcheck')
def index():
    return 'hello kubernetes'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
