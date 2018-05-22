import flask
import requests

app = flask.Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://kube-service/api/some_endpoint').json()
    return 'wow it works. Response was: {}'.format(response['data'])

@app.route('/healthcheck')
def healthcheck():
    return 'hello kubernetes'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
