import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'wow it works'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
