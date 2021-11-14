from pydantic import BaseModel
from ..TipoUsuario import TipoUsuario

class DTOCriarUsuario(BaseModel):
    tipo: TipoUsuario 
    nome: str
    ano_nascimento: int 
    mes_nascimento: int 
    dia_nascimento: int 
    email: str 
    senha: str

