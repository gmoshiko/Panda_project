#! /usr/bin/python3.4

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
from os import curdir, sep
import argparse

# Help Menu
parser=argparse.ArgumentParser(
    description='''Example: sudo service gify-panda start | stop | restart ''',
    epilog="""Listening PORT: 8090.""")
args=parser.parse_args()

PORT_NUMBER = 8090

# Class handles incoming request from the browser.
class Handler(BaseHTTPRequestHandler):

    def _set_headers(self, mimetype):
        self.send_response(200)
        self.send_header('Content-type', mimetype)
        self.end_headers()

    def do_GET(self):
        # Serving deafult index html page if nothing given.
        if self.path == "/":
            self.path = "/index.html"

        # Figuring out which type of file requested.
        try:
            BOOL = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                BOOL = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                BOOL = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                BOOL = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                BOOL = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                BOOL = True

            if BOOL == True:
                # Open static file on f and send it to the user.
                # Adding the correct Content-Type.
                f = open(curdir + sep + "resources" + self.path, 'rb')
                self._set_headers(mimetype)
                self.wfile.write(f.read())
                f.close()
            return
        # If it cant find what you want, it will give you 404 ERROR
        except IOError:
            self.send_error(404, 'Sorry, No PANDA name: %s' % self.path)

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