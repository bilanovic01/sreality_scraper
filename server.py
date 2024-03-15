from http.server import BaseHTTPRequestHandler, HTTPServer
from django.core.management import call_command
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sreality_app.settings')
            call_command('runserver')

            with open('templates/index.html', 'r') as file:
                self.wfile.write(file.read().encode('utf-8'))
        else:
            self.send_error(404)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
