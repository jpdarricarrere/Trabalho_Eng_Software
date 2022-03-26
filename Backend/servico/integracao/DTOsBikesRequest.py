from pydantic import BaseModel
from typing import Optional
from ..TipoServico import TipoServico


class DTOCriarServico(BaseModel):
    nome: str
    telefone: str
    email: str
    categoria: str
    link_imagem: str
    contratado: bool


class DTOAtualizarServico(BaseModel):
    nome: Optional[str]
    telefone: Optional[str]
    email: Optional[str]
    categoria: Optional[str]
    link_imagem: Optional[str]
    contratado: Optional[bool]
