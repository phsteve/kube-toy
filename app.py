import flask
import requests

app = flask.Flask(__name__)

@app.route('/')
def index():
    url = 'http://kube-service/api/some_endpoint'
    response = requests.get(url).json()
    return 'Response from {url} was: {response}'.format(url=url, response=response['data'])

@app.route('/healthcheck')
def healthcheck():
    return 'hello kubernetes'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
