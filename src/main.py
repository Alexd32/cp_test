from http.server import BaseHTTPRequestHandler, HTTPServer
import base64

USERNAME = "admin"
PASSWORD = "password"

class SimpleAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        auth_header = self.headers.get('Authorization')
        if not auth_header or not self.is_authenticated(auth_header):
            self.send_auth_request()
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Authorized access granted.")

    def is_authenticated(self, auth_header):
        try:
            auth_type, encoded = auth_header.split(' ', 1)
            if auth_type != 'Basic':
                return False
            decoded = base64.b64decode(encoded).decode('utf-8')
            user, pwd = decoded.split(':', 1)
            return user == USERNAME and pwd == PASSWORD
        except Exception:
            return False

    def send_auth_request(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="SimpleAuth"')
        self.end_headers()
        self.wfile.write(b"Authentication required.")

def run(server_class=HTTPServer, handler_class=SimpleAuthHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting IPA server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()