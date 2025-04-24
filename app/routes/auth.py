from app.controllers.auth.AuthController import AuthController

auth_controller = AuthController()
def auth_routes(router):
    router.get("/admin/login", auth_controller.show_login)



