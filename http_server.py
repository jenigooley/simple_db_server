#!/usr/bin/env python3

import BaseHTTPServer
import urlparse

#rite a program that runs a server that is accessible on http://localhost:4000/. 
#When your server receives a request on http://localhost:4000/set?somekey=somevalue it should store the passed key and value
#in memory. When it receives a request on http://localhost:4000/get?key=somekey it should return the value stored at somekey.

data = {}
class Request_Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def respond(self, http_code=200, http_body=""):
        self.send_response(http_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(http_body)

    def do_GET(self):

        parsed_url  =  urlparse.urlparse(self.path)
        print (parsed_url)
        p = parsed_url.path
        print ("path:", p)

        #check that path is valid
        if p not in ["/get", "/set"]:
            self.send_error(500, "Error: use /set?<key>=<val> or /get?key=<key>")
            return
        #check that query string is valid
        q_data = urlparse.parse_qs(parsed_url.query)
        if len(q_data) != 1:
            self.send_error(500, "Error: query must have a single field=value pair")
            return
        q_item = q_data.items()[0]
        q_field, q_value = q_item [0], q_item[1][0]
        print(q_item)
        print(q_field, q_value)

        #check request
        if p == "/set":
            self.set(q_field, q_value)
            self.respond(http_code=200, http_body="")
        elif p == "/get":
            if q_field != "key":
                self.send_error(500, "Error:use /get?key=<keyname> format")
                return
            value = self.get(q_value)
            if value is None:
                self.respond(http_code=404, http_body="")
                return
            self.respond(http_code=200, http_body=value)

        print (respond)

class Store_Request(Request_Handler):
    #stores data (key/value) in data dict                           
    def get(self, key):
        return data.get(key, None)
    def set (self, key, value):
        data[key] = value

def run_server():
    server_address = ('', 4000)
    http_s = BaseHTTPServer.HTTPServer(server_address,Store_Request)
    print("now serving")
    try:
         http_s.serve_forever()
    except KeyboardInterrupt:
        http_s.server_close()
        print ("connection closed")

if __name__ == '__main__':
    run_server()
