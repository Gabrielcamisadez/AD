#!/usr/bin/env python3

import http.server
import socketserver
import os

class MyhttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        filename = os.path.basename(self.path) or 'uploaded_file.zip'

        with open(filename, 'wb') as f:
            f.write(post_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'file uploaded')

        print(f"\n[+] foçe received: {filename}")

PORT = 8001

Handler = MyhttpHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"started on {PORT}")
    httpd.serve_forever()
