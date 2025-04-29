from app.utils.lib.Model import Model

class User(Model):
    def __init__(self):
        super().__init__()
        self.__table = "users"
        self.__primary_key = "id"
    
