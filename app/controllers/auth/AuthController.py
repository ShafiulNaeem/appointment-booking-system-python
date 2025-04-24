from app.utils.template import render_template
class AuthController:

    def show_login(self):
        return render_template("admin/login.html", {"title": "Login"})