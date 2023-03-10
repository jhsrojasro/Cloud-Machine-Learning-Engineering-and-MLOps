from flask import Flask, jsonify
from random import random

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/name/<value>')
def name(value):
    val = {'value': value}
    return jsonify(val)

@app.route('/random')
def random_number():
    ans = {'rand': random()}
    return jsonify(ans)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)