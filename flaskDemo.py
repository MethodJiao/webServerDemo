from flask import Flask, send_file, request
from waitress import serve
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    time.sleep(1)
    return 'Hello World'

if __name__ == '__main__':
    serve(app, host="127.0.0.1", port=8080)