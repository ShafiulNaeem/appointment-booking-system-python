from routes.auth import auth_routes
from routes.admin import admin_routes

def register_all_routes(router):
    # register auth routes
    auth_routes(router)
    # register admin routes
    admin_routes(router)