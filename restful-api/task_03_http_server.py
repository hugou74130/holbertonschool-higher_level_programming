#!/usr/bin/python3


from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json


class Handler(BaseHTTPRequestHandler):
    def _send_text(self, text, status=200):
        b = text.encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('Content-Length', str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def _send_json(self, obj, status=200):
        b = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/':
            return self._send_text("Hello, this is a simple API!")
        if path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            return self._send_json(data)
        if path == '/status':
            return self._send_text("OK")
        if path == "/info":
            info = {
                'version': "1.0",
                'description': "A simple API built with http.server",
            }
            return self._send_json(info)

        return self._send_text("Endpoint not found", status=404)


if __name__ == "__main__":
    HTTPServer(('', 8000), Handler).serve_forever()
