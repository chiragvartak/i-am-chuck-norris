#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sys import argv
from sys import exit
import subprocess
import urllib2
import json

if(len(argv) != 2):
    print 'Usage: python ' + argv[0] + ' <port-number>'
    exit(0)

PORT_NUMBER = int(argv[1])

# This class will handles any incoming request from the browser
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        json_output = urllib2.urlopen("http://api.icndb.com/jokes/random?firstName=FirstName&lastName=LastName").read()
        j = json.loads(json_output)
        self.wfile.write(j['value']['joke'])
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port' , PORT_NUMBER

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
