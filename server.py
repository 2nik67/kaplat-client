from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from flask import Flask, request, jsonify

host = "localhost"
port = 8989
app = Flask(__name__)
get_response = '45t5y6-y6y-6y6-u7i75t5-5t5t'
post_response = '1q1-3ww-2-s2–ee-ss-d'


@app.route('/test_get_method', methods=['GET'])
def do_get():
    return get_response


@app.route('/test_post_method', methods=['POST'])
def do_post():
    print(request.form['hour'])
    return jsonify({'message': post_response})


@app.route('/test_put_method', methods=['DELETE'])
def do_put():
    return "put"


@app.route('/test_delete_method', methods=['DELETE'])
def do_delete():
    return "delete"
# class Server(BaseHTTPRequestHandler):
#     def do_GET(self):
#         if 'test_get_method' in self.path:
#             params = urlparse(self.path).query
#             query_components = dict(qc.split("=") for qc in params.split("&"))
#             print(query_components['hour'])
#         self.send_response(200)
#         self.send_header('Content-type', 'text')
#         self.end_headers()
#         # Send the html message
#         self.wfile.write(bytes("45t5y6-y6y-6y6-u7i75t5-5t5t", "utf-8"))
#         return
#
#     def do_POST(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'application/json')
#         self.end_headers()
#         # Send the html message
#         self.wfile.write(bytes('{"name": "natan"}', "utf-8"))
#         return


if __name__ == '__main__':
    app.run(host=host, port=port)
    # server = HTTPServer((host, port), Server)
    # print("server starting....")
    # server.serve_forever()
    # server.server_close()
