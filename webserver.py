import json
import logging
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
from autocomplete import matcher
from constants import TERMS


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "application/json")

        # end_headers adds a blank line to denote end of headers buffer then writes to output stream
        self.end_headers()

        # Extract query param
        to_match = ''
        query_components = parse_qs(urlparse(self.path).query)
        if 'query' in query_components:
            to_match = query_components["query"][0]  # this will be the string to be matched, e.g. 'crypt'
            # maybe add some logging.error here if 'to_match' isn't in the right format

        result = matcher(to_match, TERMS)

        # The resulting list of strings need to be converted into a json bytes object to match with our Content-type
        # header.
        json_result = json.dumps(result)

        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(json_result, "utf8"))

        return


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("127.0.0.1", PORT), handler_object)

# Star the server
my_server.serve_forever()
