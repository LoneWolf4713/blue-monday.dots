import os
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Define the request handler class
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the request URL
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Extract the 'query' parameter
        query_image_href = query_params.get('query', [''])[0]

        # Send a response indicating that the request is being processed
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f'Received GET request. Processing...\n'.encode('utf-8'))

        # Execute the shell script in the background
        subprocess.Popen(['/home/prtyksh/projects/theme-changer.sh', "/home/prtyksh/Wallpapers/"+query_image_href])

# Define the server parameters
server_address = ('', 56000)  # Empty string for localhost

# Create the HTTP server
httpd = HTTPServer(server_address, RequestHandler)

# Start the HTTP server
print('Starting server...')
httpd.serve_forever()
