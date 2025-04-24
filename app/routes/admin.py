from app.controllers.SlotController import SlotController

slotController = SlotController()

def admin_routes(router):
    router.get("/admin/slots", slotController.index)