import json
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
from autocomplete import matcher
from constants import TERMS


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Create a RequestHandler class which inherets from SimpleHTTPRequestHandler.
    """
    def create_trie(self):
        # sort check of TERMS list
        # create 'my_trie' by instantiating Trie tree
        # run import of TERMS into 'my_trie'
        pass
        # ADD AN INIT(?) METHOD THAT INITIALISES THE TRIE TREE ONLY ONCE SO NOT DONE EVERY TIME THERE IS A GET REQUEST

    def do_GET(self):

        self.send_response(200)  # OK response
        self.send_header("Content-type", "application/json")  # set the header
        # end_headers adds a blank line to denote end of headers buffer then writes it to output stream
        self.end_headers()

        # get the query string value
        query_components = parse_qs(urlparse(self.path).query)
        to_match = ''
        if 'query' in query_components:
            to_match = query_components["query"][0].lower()  # string to be matched, e.g. 'crypt'

        if len(to_match) > 0:
            result = matcher(to_match, TERMS)  # get the first 4 sorted elements that match
            # call my_trie.prefix_search(to_match)
        else:
            result = ''

        # convert result into a JSON string object as Content-type header is application/json.
        json_result = json.dumps(result)

        # convert JSON string into bytes object and write to output stream.
        self.wfile.write(bytes(json_result, "utf8"))


# instantiate RequestHandler
handler_object = RequestHandler
# handler_object.create_trie()

PORT = 8000
my_server = socketserver.TCPServer(("127.0.0.1", PORT), handler_object)

# run the server
my_server.serve_forever()
