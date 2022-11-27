from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from flask import Flask, request, jsonify

host = "localhost"
port = 8989
app = Flask(__name__)
get_response = '45t5y6-y6y-6y6-u7i75t5-5t5t'
post_response = '1q1-3ww-2-s2–ee-ss-d'
put_response = 'hhfg7rt5-t5–grn-h-j7-6ygr'


@app.route('/test_get_method', methods=['GET'])
def do_get():
    return get_response


@app.route('/test_post_method', methods=['POST'])
def do_post():
    return jsonify({'message': post_response})


@app.route('/test_put_method', methods=['PUT'])
def do_put():
    return jsonify({"message": put_response})


@app.route('/test_delete_method', methods=['DELETE'])
def do_delete():
    return "delete"


if __name__ == '__main__':
    app.run(host=host, port=port)
