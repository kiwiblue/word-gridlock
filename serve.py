import os, sys
os.chdir('/Users/actionvideo/Documents/+Claude/Games/Scramble')
from http.server import HTTPServer, SimpleHTTPRequestHandler
HTTPServer(('', 3456), SimpleHTTPRequestHandler).serve_forever()
