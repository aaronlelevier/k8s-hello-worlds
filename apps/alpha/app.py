import flask
import requests

app = flask.Flask(__name__)

@app.route('/')
def home():
   return flask.jsonify({'hello': 'alpha'})

@app.route('/<service>')
def service(service):
    r = requests.get(f"http://{service}.default.svc.cluster.local:5000")
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
