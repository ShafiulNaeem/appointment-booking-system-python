from app.utils.lib.ValidationRules import ValidationRules
class RegistrationRequest:
    def __init__(self, request):
        self.request = request
        self.rules = {
            "name": ["required", "string", "max:255"],
            "email": ["required", "email", "string"],
            "login[password]": ["required", "string", "min:6", "max:8"],
            "image": ["required", "file", "extention:pdf","max_size:2048", "min_size:1024"],
        }
        
        self.errors = ValidationRules.validate(self.request,self.rules)
        return self.errors if self.errors else None
        
        