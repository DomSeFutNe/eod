import uuid

class GenerateApiId:
    def generate(self, prefix: str):
        return f"{prefix}_{str(uuid.uuid4())}"
    
def character_id():
        return GenerateApiId().generate("char")
    
def user_id():
        return GenerateApiId().generate("user")
    
def server_list_id():
        return GenerateApiId().generate("seli")