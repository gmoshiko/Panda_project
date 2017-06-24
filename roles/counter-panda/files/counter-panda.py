#! /usr/bin/python3.4

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
from os import curdir, sep
import argparse

# Help Menu
parser=argparse.ArgumentParser(
    description='''Example: sudo service counter-panda start ''',
    epilog="""Listening PORT: 8100.""")
args=parser.parse_args()

PORT_NUMBER = 8100
COUNTER = 0

# Class handles incoming request from the browser.
class Handler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # Giving number of POST request was made.
        self._set_headers()
        self.wfile.write(bytes("number of post: " + str(COUNTER), "utf-8"))

    def do_POST(self):
        # Counter for POST request.
        global COUNTER
        COUNTER += 1
        self._set_headers()
        self.wfile.write(bytes("I SEE YOU -_- ", "utf-8"))

if __name__ == "__main__":
    try:
        # Create an HTTP server and define the handler.
        server = HTTPServer(('', PORT_NUMBER), Handler)
        print('The Http server is ready, localhost:%s' % PORT_NUMBER)
        server.serve_forever()

    except KeyboardInterrupt:
    	# kill proccess on Control-C
        print('Shutting down the Server!')
        server.socket.close()