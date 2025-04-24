class Router:
    def __init__(self):
        self.routes = {
            "GET": {},
            "POST": {},
            "PUT": {},
            "DELETE": {}
        }

    def get(self, path, handler):
        self.routes["GET"][path] = handler
    
    def post(self, path, handler):
        self.routes["POST"][path] = handler
    
    def put(self, path, handler):
        self.routes["PUT"][path] = handler
    
    def delete(self, path, handler):
        self.routes["DELETE"][path] = handler
    
    def handle_request(self, method, path, form=None):
        handler = self.routes.get(method, {}).get(path) 
        # print(handler())
        if handler:
            return handler(form) if form else handler() ,200
        else:
            return "404 Not Found", 404
        
    
  