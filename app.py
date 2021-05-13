# code that launches the application lives here, but this should be mostly empty
from flask import Flask, jsonify
from routes import *

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(about='Hello, RNAgora!')

if __name__ == '__main__':
    # TODO replace with the same port as in the Dockerfile
    app.run(host="localhost", debug=True, port=5000) 