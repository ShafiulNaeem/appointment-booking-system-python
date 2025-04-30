from app.controllers.auth.AuthController import AuthController

auth_controller = AuthController()
def auth_routes(router):
    router.get("/admin/login", auth_controller.show_login)
    router.get("/admin/register", auth_controller.show_register)
    router.post("/admin/register/store", auth_controller.register)



