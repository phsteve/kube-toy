import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'hello world!!!!! we just built an image from a new commit'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
