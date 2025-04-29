from app.utils.middleware.AcceptFile import AcceptFile
from app.utils.lib.template import error404

class Router:
    def __init__(self):
        self.routes = {
            "GET": {},
            "POST": {},
            "PUT": {},
            "DELETE": {}
        }
        self.acceptFile = AcceptFile()

    def get(self, path, handler):
        self.routes["GET"][path] = handler
    
    def post(self, path, handler):
        self.routes["POST"][path] = handler
    
    def put(self, path, handler):
        self.routes["PUT"][path] = handler
    
    def delete(self, path, handler):
        self.routes["DELETE"][path] = handler
    
    def handle_request(self, method, path, form=None):
        # Check if the path is a file request
        content, mime_type, status = self.acceptFile.handle_file(path)
        if status == 200:
            headers = {"Content-Type": mime_type}
            return content, headers, 200
        elif status == 404 and (path.startswith("/static") or path.startswith("/assets")):
            return b"Static File Not Found", {"Content-Type": "text/plain"}, 404

        handler = self.routes.get(method, {}).get(path) 
        if handler:
            response = handler(form) if form else handler()
            headers = {"Content-Type": "text/html"}
            return response, headers,200
        else:
            return error404(), {"Content-Type": "text/html"}, 404
        
    
  