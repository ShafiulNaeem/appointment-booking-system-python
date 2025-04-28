import os
from app.utils.lib.File import File

class AcceptFile(File):
    def __init__(self):
        self.base_path = os.getcwd()

    def handle_file(self,path):
        if path.startswith("/"):
            path = path[1:]
        
        file_path = os.path.join(self.base_path, path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                content = file.read()
            mime_type = self.get_mime_type(file_path)
            return content,mime_type, 200
        else:
            return None, None, 404
    

