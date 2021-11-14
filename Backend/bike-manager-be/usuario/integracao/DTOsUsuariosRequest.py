from pydantic import BaseModel
from typing import Optional
from ..TipoUsuario import TipoUsuario

class DTOCriarUsuario(BaseModel):
    tipo: TipoUsuario 
    nome: str
    ano_nascimento: int 
    mes_nascimento: int 
    dia_nascimento: int 
    email: str 
    senha: str

class DTOAtualizarUsuario(BaseModel):
    id: Optional[int] = None
    tipo: Optional[TipoUsuario] = None
    nome: Optional[str] = None
    ano_nascimento: Optional[int] = None
    mes_nascimento: Optional[int] = None
    dia_nascimento: Optional[int] = None
    email: Optional[str] = None 
    senha: Optional[str] = None

