#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

import http.server
import socketserver

# Define the host and port on which you want to run the server
HOST = "0.0.0.0"
PORT = 8000


socketserver.TCPServer.allow_reuse_address = True


# Define a request handler class by subclassing BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # Handler for GET requests
    def do_GET(self):
        """
        Handles GET requests sent to the server.

        Sends a response with a simple HTML page containing "Hello, World!".
        """
        self.send_response(200)  # Response code 200: OK
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # HTML content to be served
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Python Web Server</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple web server implemented in Python.</p>
        </body>
        </html>
        """

        # Send the HTML response
        self.wfile.write(html_content.encode("utf-8"))


# Create an instance of the HTTP server with our handler class
with socketserver.TCPServer((HOST, PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Server started at {HOST}:{PORT}")

    # Start the server and keep it running until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped")
