import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
   return flask.jsonify({
        'name': 'charlie',
        'version': 1,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0")
