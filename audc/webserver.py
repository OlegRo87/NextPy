from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    def do_get(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello World'.encode())


def main():
    hostname = "localhost"
    port = 8000
    server = HTTPServer((hostname, port), HelloHandler)
    print('Server running on port %s' % port)
    server.serve_forever()


if __name__ == '__main__':
    main()
