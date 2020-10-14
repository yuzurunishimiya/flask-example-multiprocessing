from flask import Flask, jsonify

from connection import session
from connection import db_data
from processing_sub import doMultiProcessing

import multiprocessing
import json
import requests

app = Flask(__name__)


# GET TIME OF 
@app.route("/get-time/<key>")
def restime(key):
    c = session.ttl(key)
    return jsonify({
        "key": key,
        "remaining time": str(c) + " seconds"
    })


@app.route("/get-context")
def get_context():
    data = list(db_data.find({},{"_id": 0}).limit(50000))
    return json.dumps(data)


@app.route("/get/<key>")
def index(key):
    data = session.get(key)
    if data:
        return jsonify(data=json.loads(data))
    thread = multiprocessing.Process(target=doMultiProcessing, args=(key,))
    thread.start()
    r = requests.get("http://localhost:5000/get-context")
    return jsonify(data=json.loads(r.text))


@app.route("/")
def index_():
    return jsonify({
        "status": "ok",
        "action": "go redirect to '/get/<key>'"
    })


if __name__ == "__main__":
    app.run(debug=True)
