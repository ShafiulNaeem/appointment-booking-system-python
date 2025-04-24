from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from app.core.router import Router
from app.routes import register_all_routes


# Initialize the router
router = Router()
register_all_routes(router)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response, status = router.handle_request("GET", self.path)
        print(f"Rift GET request for {self.path} - Status: {status} - Response: {response}")
        self.respond(response, status)

    
    def do_POST(self):
        form = self.get_post_data()
        response, status = router.resolve("POST", self.path, form)
        self.respond(response, status)

    def do_PUT(self):
        form = self.get_post_data()
        response, status = router.resolve("PUT", self.path, form)
        self.respond(response, status)

    def do_DELETE(self):
        form = self.get_post_data()
        response, status = router.resolve("DELETE", self.path, form)
        self.respond(response, status)

    def do_PATCH(self):
        form = self.get_post_data()
        response, status = router.resolve("PATCH", self.path, form)
        self.respond(response, status)

    def get_post_data(self):
        content_length = int(self.headers.get('Content-Length', 0))
        raw_data = self.rfile.read(content_length).decode()
        return {k: v[0] for k, v in parse_qs(raw_data).items()}

    def respond(self, response, status=200):
        self.send_response(status)
        self.end_headers()
        self.wfile.write(response.encode())

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Rift starting server on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
