from app.utils.lib.template import render_template
from app.validation.RegistrationRequest import RegistrationRequest
class AuthController:

    def show_login(self):
        return render_template("admin/auth/login.html", {"title": "Login | ABS Admin"})
    
    def show_register(self):
        return render_template("admin/auth/register.html", {"title": "Register | ABS Admin"})
    
    def register(self, request):
        validate = RegistrationRequest(request)
        
