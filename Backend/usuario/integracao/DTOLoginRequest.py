from pydantic import BaseModel

class DTOLoginRequest(BaseModel):
    email: str 
    senha: str

